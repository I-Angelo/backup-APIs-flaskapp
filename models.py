# HElps us with databases . Automate data bases

from flask_sqlalchemy import SQLAlchemy #handle our data and pass it back and forth between our application and our database 
from flask_migrate import Migrate  #data tables
import uuid #universal unique identifier (string of numbers for primary keys. Keeps things unique. If there is two people with the same name, 
            #this will produce two different id_numbers)
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash # packages meant to encrypt our password even inside my own database for security
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow #Which also helps moving data back and forth particularly if we have a collection of data 
import secrets

# set variables for class instantiation 
login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

# Decorator is called '@'. Its like writting a route
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


    ##THIS WHOLE CLASS IS FOR THE USERS TO CREATE ACCOUNTS AND LOGIN

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)  # This 'id' is very usefull beacuse we want to make sure this ID is the users primary key and not 
                                                    # their beacuse what if we have two or more people with the same name 
    first_name = db.Column(db.String(150), nullable=True, default='') # 'nullable is equal to saying 'not Null'.  
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False) #In this case nullable is True because an email is absoutely necessary. In name and last name
                                                        #we are allowed to have empty spaces
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True ) #Token is unique to each user. To gatekeep who is accessing our stuff and make sure they are allowed
                                                            #This token is generated when someone creates an account and when some one want to access
                                                            # the phonebook, it is someone that created an account and not someone random
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow) #When the account is created the date is generated



    #This is essentil in every class just like __init__ in python
    def __init__(self, email, first_name='', last_name='', password='', token='', g_auth_verify=False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length): # as it is in the __init__ above , the length is 24 characters 
        return secrets.token_hex(length) #security.token_hex module generates a random strong number that is used for security tokens

    def set_id(self):
         return str(uuid.uuid4()) #when this function runs it will generate an ID for our user with numbers and letters that will be unique and 
                                # that would be a primary key that is its own entity

    def set_password(self, password): #here the parameter password is the one provided by our user
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash #this hashes the password for security

    def __repr__(self): #This is used as a confirmation that what we wanted to happen with all the classes just happened
        return f'User {self.email} has been added to the database'


    ##THIS CLASS IS OF THE ACTUAL CONTACTS IN OUR DATABASE THAT WE ARE STORING

class Recipe(db.Model):
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String(150), nullable = False)
    ingredients = db.Column(db.String(700))
    instruction = db.Column(db.String(1000))
    notes = db.Column(db.String(1000))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, name, ingredients, instructions, notes, user_token, id=''):
        self.id = self.set_id()
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.notes = notes
        self.user_token = user_token


    def __repr__(self):
        return f'The following Recipe has been added to the phonebook: {self.name}'

    def set_id(self):
        return (secrets.token_urlsafe())


class RecipeSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'ingredients', 'instructions', 'notes']


recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many = True)


   
































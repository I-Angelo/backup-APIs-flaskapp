#these are the routes we use to pass the information into the database

from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Recipe, recipe_schema, recipes_schema

api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/getdata')
def getdata():
    return {'yee': 'haw'}


@api.route('/myrecipes', methods = ['POST'])
@token_required
def create_contact(current_user_token):
    name = request.json['name'] # All of these are the key for the key-value pair dictionary
    ingredients = request.json['ingredients']
    instructions = request.json['instructions']
    notes = request.json['notes']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    recipe = Recipe(name, ingredients, instructions, notes, user_token = user_token) #'Recipes' comes from modules.py

    db.session.add(recipe) #This is how we start the session to add the recipe to our database
    db.session.commit() #This works like Github push, and to send the data we need to commit it

    response = recipe_schema.dump(recipe)
    return jsonify(response)
    #The last two lines of code will return the information that was just stored in the database. .dump and schema are part of 
    #marshmallow. Remember the contact_schema comes from 'models.py (vehicle_schema = VehicleSchema()
    #vehicles_schema = VehicleSchema(many = True)) This will show in insomnia and help us testing our API

@api.route('/myrecipes', methods = ['GET'])
@token_required
def get_contact(current_user_token):
    a_user = current_user_token.token
    recipes = Recipe.query.filter_by(user_token = a_user).all()
    response = recipes_schema.dump(recipes)
    return jsonify(response)

# Get single recipe or endpoint
@api.route('/myrecipes/<id>', methods = ['GET']) #<id> . anything you put inisde the braces is a variable that we can call 
@token_required
def get_single_contact(current_user_token, id): #here we are passing the 'id' variable referenced in line 45
    recipe = Recipe.query.get(id)
    response = recipe_schema.dump(recipe)
    return jsonify(response)

# Update endpoint
@api.route('/myrecipes/<id>', methods = ['POST', 'PUT']) #Because it is an update we neewd to PUT and POST
@token_required
def update_contact(current_user_token, id): #here we are passing the 'id' variable referenced in line 53
    recipe = Recipe.query.get(id)
    recipe.name = request.json['name']
    recipe.ingredients = request.json['ingredients']
    recipe.instructions = request.json['instructions']
    recipe.notes = request.json['notes']
    recipe.user_token = current_user_token.token

    db.session.commit()
    response = recipe_schema.dump(recipe)
    return jsonify(response)

# Delete Method or endpoint
@api.route('/myrecipes/<id>', methods = ['DELETE'])
@token_required
def delete_contact(current_user_token, id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    response = recipe_schema.dump(recipe)
    return jsonify(response)


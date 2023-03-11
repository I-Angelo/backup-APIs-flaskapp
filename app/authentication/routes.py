from forms import UserLoginForm
from models import User, db, check_password_hash
from flask import Blueprint, render_template, request, redirect, url_for, flash

#imports for flask login
from flask_login import login_user, logout_user, LoginManager, current_user, login_required 

auth = Blueprint('auth', __name__, template_folder = 'auth_templates')

##SIGNUP METHOD

@auth.route('/signup', methods = ['GET', 'POST']) #This are HTML methods to request and submit user data to the servers
def signup():
    form = UserLoginForm() #This comes from 'forms.py' and instantiates the class in that file (see file)

    try:
        if request.method == 'POST' and form.validate_on_submit(): #validate_on_submit comes from forms.py from the import wtfforms.validators
                                                                    #POST means that user submitted that data
            email = form.email.data #This type of information like email and password was entered in the forms.html and ran through forms.py for 
                                    #validation and then if its valid, it will be stored in the 'email' variable. Hence 'form' coming from the (html), etc
            password = form.password.data # same thing for password
            print(email, password)

            user = User(email, password = password) #We are instantiating the 'User' class from models.py

            db.session.add(user)
            db.session.commit()

            flash(f'You have succesfully created a user account {email}', 'User-created') #flash is part of flask. Its for a quick message at the end 
                                                                                # of a request once
            return redirect(url_for('site.home')) #this will redirect and url-for will go and look for 'site' in site/routes.py/home
            #In this case , after the user has created their account, they qwill be redirtected to the home page
    except:
        raise Exception('Invalid for data: Please check your form')
    return render_template('sign_up.html', form = form) #It will redirect the user to the signup form(html) for the data to be verified through
                                                        #forms.py once again. Itll keep asking the user for valid data

###SIGNIN METHOD

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit(): #same verification process as in our 'SIGNUP METHOD' above
            email = form.email.data
            password = form.password.data
            print(email, password)

            logged_user = User.query.filter(User.email == email).first() #here we are taking the email and check it against the 'User' class in mopdels.py
                                                                        #and query our database, filter the data and pull the 'first()' user with that email,
                                                                        #and this will be our logged user and hold on to this user. Should pull back 1 acct

            if logged_user and check_password_hash(logged_user.password, password): #chk_pass_hash takes 2 parameters 1. the hashed pass from user when they
                                                                #signed up, then de-hash it and, 2. the passwrd they are entering now and compare them both 
                                                                #and see if it is accurate. check if the credentials are correct.
                                                                #Also, 'if looged_user' (TRUE statement) is checking if the email is in the datebase. If not ,
                                                                #this 'if-statement' would be false to begin with.
                login_user(logged_user) #We imported from flask_login and passed the variable above in line 50
                flash('You were succesful in your initiation. Congratulations, and welcome to the Jedi Knights', 'auth-success')
                return redirect(url_for('site.profile'))
            else:
                flash('You have failed in your attempt to access this content.', 'auth-failed')
    except:
        raise Exception('Invalid form data: Please check your form')
    return render_template('sign_in.html', form = form)


##LOGOUT METHOD

@auth.route('/logout')
def logout():
    logout_user() #this is another method part of flask
    return redirect(url_for('site.home')) #sending user back to home after being logged out
        
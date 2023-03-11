from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder = 'site_templates') #The variable 'site'
                                            #is importing the contents of 'site_templates' as it is 
                                            #one of the arguments for the instatiation of the Blueprint class as 'site'.
                                            #This is being called in our file '__init__' on line 5

# this file determines how the page will ultimately end up being rendered. All these file are inside the 'site' folder. This is the 
# 'idea' of the website but it wont do anything until it is called by '__init__.py'. So basically the line of code on line 3 , it is the instatiation
# or blueprint of the website, just like a class in python

@site.route('/')
def home():
    return render_template('index.html') #When we run flask this is our default page wil load index.html with our base.html built around it 

# We are coming from '__init__.py' and the above code is 'home'. It renders 'index.html' along with 'base.html'

@site.route('/profile')
def profile():
    return render_template('profile.html')




# Alows our application to talk to the internet and all systems it may be ran

import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__)) 
load_dotenv(os.path.join(basedir, '.env'))

# this lines can be always copy-pasted . It allows the application to run and talk to the computers
# Allows our app talk to the operating system
                                                    
class Config():
    '''
        Set config variables for the flask app
        using Environment variables where available.
        Otherwise, create the config variable if not done already.
    '''

    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Starfish' #The first three lines of code is our app talking to the computer 
    # The code below is how the app talks to the database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_NOTIFICATIONS = False 



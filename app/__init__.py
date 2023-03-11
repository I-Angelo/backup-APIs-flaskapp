### This file is the decision making process. 

from flask import Flask #Here is where we import flask for our application
from config import Config
# Now we need to import all of the files and folders for the website located in the folder 'site'
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db as root_db, login_manager, ma 
from flask_cors import CORS
from helpers import JSONEncoder

app = Flask(__name__)
CORS(app) # This is used for enhanced security against hackers

app.register_blueprint(site) #This calls 'routes.py' and subsequently 'home' instance .( see routes.py/home)
app.register_blueprint(auth)
app.register_blueprint(api)

app.json_encoder = JSONEncoder
app.config.from_object(Config)
root_db.init_app(app) #initiates the app
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)
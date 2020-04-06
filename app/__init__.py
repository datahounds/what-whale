from flask import Flask
from flask_bootstrap import Bootstrap
import os
# from app.config import Config


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

app = Flask(__name__)
Bootstrap(app)
app.config['STATIC_DIR'] = STATIC_DIR
# app.config.from_object(Config)

# since routes needs to import the app variable from this script
# we use a bottom import to avoid the error that results from
# mutual references between the two files
from app import routes

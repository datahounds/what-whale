from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__)
Bootstrap(app)
app.config.from_object(Config)

# since routes needs to import the app variable from this script
# we use a bottom import to avoid the error that results from
# mutual references between the two files
from app import routes, classifier

# Main application package

# Import libraries
from flask import Flask

# Create object instances
app = Flask(__name__)

# Dev secret Key
app.secret_key = 'devmodeenagged'

# Import the routes
from flask_basics import routes

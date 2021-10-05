# Main application package

# Import libraries
from flask import Flask

# Create object instances
app = Flask(__name__)

# Import the routes
from flask_basics import routes

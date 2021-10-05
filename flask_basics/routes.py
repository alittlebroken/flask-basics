# Application main routing

# Imports
from flask_basics import app
from flask import render_template

# Routing
@app.route("/")
def index():
    return "<h1>This is the home page bitches!!!!</h1>"

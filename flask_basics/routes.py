# Application main routing

# Imports
from flask_basics import app
from flask import render_template

# Routing
@app.route("/")
def index():
    return render_template("index.html", title="Brintey Bitches!!!")

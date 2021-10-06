# Application main routing

# Imports
from flask_basics import app
from flask import render_template, request

# Routing
@app.route("/")
def index():
    return render_template("index.html", title="Brintey Bitches!!!")

@app.route("/register", methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        return '''
                <h1>Submitted Form Data</h1>
                <p>Username: {}</p><br>
                <p>Email: {}</p><br>
                <p>Password: {}</p><br>
               '''.format(username, email, password)

    return '''
            <form method="POST">
            <div><label>Username: </label><input type="text" name="username"></div>
            <div><label>Email: </label><input type="email" name="email"></div>
            <div><label>Password: </label><input type="password" name="password"></div>
            <div><label>Confirm Password: </label><input type="password" name="confirm-password"></div>
            <div><input type="submit" value="Submit">
            </form>
           '''

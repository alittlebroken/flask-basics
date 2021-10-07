# Application main routing

# Imports
from flask_basics import app
from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template, request, flash, redirect, url_for, session

# Test data
users = [
    {
        'username': 'paul',
        'id': 1,
        'email': 'plockyer@googlemail.com',
        'password': generate_password_hash('password', 'sha256')
    },
    {
        'username': 'yvette',
        'id': 2,
        'email': 'ylp1980@outlook.com',
        'password': generate_password_hash('bogboobedredheads', 'sha256')
    }
]

# Routing


@app.route("/")
def index():
    return render_template("index.html", title="Brintey Bitches!!!")


@app.route("/register", methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        username = request.form.get('username', None)
        email = request.form.get('email', None)
        password = request.form.get('password', None)
        confirm_password = request.form.get('confirm-password', None)

        if not username or username == '' or username is None:
            flash('You must enter a username')
            return redirect(url_for('register'))

        if not email or email == '' or email is None:
            flash('You must enter a valid email address')
            return redirect(url_for('register'))

        if not password or password == '' or password is None:
            flash('You must supply a password')
            return redirect(url_for('register'))

        if password != confirm_password:
            flash('Password and confirm password must match')
            return redirect(url_for('register'))

        # Check if user does not already exist
        for user in users:
            if user["username"] == username:
                flash('This user already exists, please login instead.')
                return redirect(url_for('login'))

        # Add the user to the users list
        users.append({
            'username': username,
            'id': users.length() + 1,
            'email': email,
            'password': generate_password_hash(password, 'sha256')
            })
        flash('User successfully added, please now login.')

        return redirect(url_for('login'))

    return render_template("register.html", title="Registration form")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)

        if not username or username == '' or username is None:
            flash('You must enter in a valid username')
            return redirect(url_for('login'))

        if not password or password == '' or password is None:
            flash('You must enter in a valid password')
            return redirect(url_for('login'))

        # Check if the user exists
        for item in users:
            if item["username"] == username:
                if check_password_hash(item["password"], password):
                    session["id"] = item["id"]
                    session["name"] = item["username"]
                    session["isLoggedIn"] = True
                    return redirect(url_for('index'))
                else:
                    flash('are you sure that password is correct?')
                    return redirect(url_for('login'))

        flash('That user does not exist please register')
        return redirect(url_for('register'))

    return render_template("login.html", title="Login Screen")


@app.route("/logout")
def logout():
    session["id"] = 0
    session["username"] = 'Anon'
    session["isLoggedIn"] = False

    return redirect(url_for('login'))


@app.route("/users")
def user_list():
    return render_template(
        "userlisting.html",
        title="Current Users",
        users=users)


@app.route("/profile")
def profile():

    for user in users:
        if user["id"] == session["id"]:
            current_user = user

    return render_template(
                            "profile.html",
                            title="Profile for {}".format(session["name"]),
                            user=current_user
                          )

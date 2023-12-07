from flask import Blueprint, render_template, request, flash, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import login_user

from models import User
from db import db
from data import USERS

from flask import session


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Can get Data from database
    #user = User.query.filter_by(username=username).first()

    # Retrieving data from Hardcode dict of User object
    user = USERS.get(username)

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    login_user(user)

    print(f"User ID in session: {session.get('_user_id')}")

    return redirect(url_for('main.index'))

#A Blueprint is essentially a way to define a set of routes, views, and other application-related components in a modular manner. 
# It helps to split a Flask application into reusable components, making the codebase more maintainable and extensible.
from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"
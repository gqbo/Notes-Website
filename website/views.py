# Store the standard routes to our website, where users can actually go to.

#A Blueprint is essentially a way to define a set of routes, views, and other application-related components in a modular manner. 
# It helps to split a Flask application into reusable components, making the codebase more maintainable and extensible.
from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/') # Defines a runs the 'home page' when we call the root URL
def home():
    return "<h1>Test!<h1>"






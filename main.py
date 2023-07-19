from website import create_app # We can do this because the website folder is a python package, because we have the __init__.py file.

app = create_app()

if __name__ == '__main__': # Only if we run the main.py file it will run the web server. If we import main.py in another file it would not run the web server.
    app.run(debug=True) # Runs a local development server. 
    # Debug is set to true because we want to automatically rerun the web server if we change some code.
    # In production we don't want debug set to true.


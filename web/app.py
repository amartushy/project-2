"""
Adrian Martushev's Flask API.
"""

import os
from flask import Flask, render_template

app = Flask(__name__)


def file_exists(filename):
    file_path = os.path.join("web/templates", filename)
    return os.path.isfile(file_path)

# Function to serve files or return an error page
def serve_file_or_error(filename, error_page):
    if '..' in filename or '~' in filename:
        # Handle illegal characters in the filename
        return "File is forbidden!", 403

    if file_exists(filename):
        # Serve the requested file
        return render_template(filename)
    else:
        # Serve the appropriate error page
        return render_template(error_page)
        
        
@app.route("/")
def hello():
    return "UOCIS docker demo!\n"
    
    
@app.route("/404.html")
def pageNotFound():
    return render_template('404.html')

@app.route("/403.html")
def pageError():
    return render_template('403.html')


@app.route("/trivia.html")
def trivia():
    return render_template('trivia.html')
    
    
   
        

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


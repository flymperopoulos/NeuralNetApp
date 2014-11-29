import os
from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

@app.route('/', methods=['POST','GET'])
def home(): 
    """Render website's home page."""
    if request.method == 'POST':
        print request.form.get('data')
    return render_template('home.html')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
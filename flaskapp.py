import os
from flask import Flask, render_template, request, redirect, url_for
import csv
import json
import numpy as np
from skimage.io import imsave
from skimage.transform import resize


app = Flask(__name__)

# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

def unit_scale(x, eps=1e-8):
    """ Scales all values in the ndarray ndar to be between 0 and 1 """
    x = x.copy()
    x -= x.min()
    x *= 1.0 / (x.max() + eps)
    return x

def get_boolean(img):
    img = img.astype('float32')
    img = unit_scale(img)
    img = resize(img, (100,100))
    img = img > 0
    return img

@app.route('/', methods=['POST','GET'])
def home(): 
    """Render website's home page."""
    if request.method == 'POST':
        data = request.form.get('data')
        arr = json.loads(data)
        bool_img = get_boolean(np.array(arr))
        print bool_img
        
        # print img.shape

        name = 'bool'
        
        # print type(img)
        np.save('smarterboard-images/' + name, boolimg)
        # imsave(img, 'smarterboard-images/' + name)


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

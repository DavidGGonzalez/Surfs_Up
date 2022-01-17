# URL to Canvas page: https://courses.bootcampspot.com/courses/976/pages/9-dot-4-3-set-up-flask-and-create-a-route?module_item_id=358681
# Python Magic Methods: https://www.geeksforgeeks.org/dunder-magic-methods-python/
# Flask: https://flask.palletsprojects.com/en/2.0.x/

# Flask
from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define starting or root
@app.route('/')
# Create a function
def hello_world():
    return 'Hello World'

@app.route('/about')
def about():
    print('Accessing the About page (Route)')
    return "Hi, my name is <b>David G Gonzalez</b><br>and this is my first <b>FLASK page</b>"


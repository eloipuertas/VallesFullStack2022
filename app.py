"""Flask application setup."""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# create flask app
app = Flask(__name__)
CORS(app)   # enable CORS
#create connection to database sqlite file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

"""add main root route"""
@app.route('/')
def index():
    """add main root route"""
    return 'Hello World'


#run app
if __name__ == '__main__':
    app.run(debug=True)






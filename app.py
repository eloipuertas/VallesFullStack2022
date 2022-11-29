"""Flask application setup."""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
#create jsonify method to return json response
from flask import jsonify
#get request object
from flask import request


# create flask app
app = Flask(__name__)
CORS(app)   # enable CORS
#create connection to database sqlite file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

""" 
Models 
Create a Disk model with title, artist, and genre fields
"""
class Disk(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    artist = db.Column(db.String(80), nullable=False)
    genre = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'{self.title} by {self.artist}'

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "artist": self.artist,
            "genre": self.genre
        }
    
""" add main root route """
@app.route('/')
def index():
    """add main root route"""
    return 'Hello World'

""" GET endpoint for all Disks in the model """
@app.route('/disks', methods=['GET'])
def get_disks():
    """get all disks"""
    disks = Disk.query.all()
    return jsonify([disk.serialize() for disk in disks]), 200

""" GET endpoint for a single Disk in the model """
@app.route('/disks/<int:id>', methods=['GET'])  # type: ignore
def get_disk(id):
    """get single disk"""
    disk = Disk.query.get(id)
    return jsonify(disk.serialize()), 200

""" POST endpoint for Disk model """
@app.route('/disks', methods=['POST'])  # type: ignore
def create_disk():
    """create a disk"""
    request_body = request.get_json()
    new_disk = Disk(
        title=request_body['title'],
        artist=request_body['artist'],
        genre=request_body['genre']
    )
    db.session.add(new_disk)
    db.session.commit()
    return jsonify(new_disk.serialize()), 200

""" PUT endpoint for Disk model """
@app.route('/disks/<int:disk_id>', methods=['PUT'])  #   type: ignore
def update_disk(disk_id):
    """update a disk"""
    request_body = request.get_json()
    disk = Disk.query.get(disk_id)
    disk.title = request_body['title']
    disk.artist = request_body['artist']
    disk.genre = request_body['genre']
    db.session.commit()
    return jsonify(disk.serialize()), 200
""" DELETE endpoint for Disk model """
@app.route('/disks/<int:disk_id>', methods=['DELETE'])  # type: ignore
def delete_disk(disk_id):
    """delete a disk"""
    disk = Disk.query.get(disk_id)
    db.session.delete(disk)
    db.session.commit()
    return jsonify(disk.serialize()), 200


#create models in database with context manager
with app.app_context():
    db.create_all()
        
#run app
if __name__ == '__main__':
    app.run(debug=True)






""" Flask application setup"""  
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



#add main root rout
@app.route('/')
def index():
    return 'Hello World'


"""
Models,
Create a Disk model with the following fields:
    - id (primary key)
    -title (string)
    -artist (string)
    -genre (string)
    """

class Disk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    artist = db.Column(db.String(80), nullable=False)
    genre = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Disk %r>' % self.title

""" GET endpoint to get all disks """
@app.route('/disks', methods=['GET'])
def get_disks():
    disks = Disk.query.all()
    return {'disks': [disk.serialize() for disk in disks]}

""" GET endpoint to get a single disk """
@app.route('/disks/<int:id>', methods=['GET'])
def get_disk(id):
    disk = Disk.query.get(id)
    return disk.serialize()

""" POST endpoint to create a disk """
@app.route('/disks', methods=['POST'])
def create_disk():
    disk = Disk(title=request.json['title'], artist=request.json['artist'], genre=request.json['genre'])
    db.session.add(disk)
    db.session.commit()
    return disk.serialize()

""" PUT endpoint to update a disk """
@app.route('/disks/<int:id>', methods=['PUT'])
def update_disk(id):
    disk = Disk.query.get(id)
    disk.title = request.json['title']
    disk.artist = request.json['artist']
    disk.genre = request.json['genre']
    db.session.commit()
    return disk.serialize()

""" DELETE endpoint to delete a disk """
@app.route('/disks/<int:id>', methods=['DELETE'])
def delete_disk(id):
    disk = Disk.query.get(id)
    db.session.delete(disk)
    db.session.commit()
    return disk.serialize()

#initailize the database
db.create_all()

#initialize the app
if __name__ == '__main__':
    app.run(debug=True)





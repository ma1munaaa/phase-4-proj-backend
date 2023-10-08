from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Tm
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///checkin.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)

@app.route("/tms", methods=['GET'])
def get_tms():
    tms = Tm.query.all()
    return jsonify([tm.to_dict() for tm in tms])

@app.route("/add-tm", methods=['POST'])
def create_tm():
    data = request.get_json()
    tm = Tm(Name=data.get('Name'), Phone=data.get('Phone'), Email=data.get('Email'))
    db.session.add(tm)
    db.session.commit()
    return make_response(
        jsonify({'id': tm.id, 'Name': tm.Name, 'Phone': tm.Phone, 'Email': tm.Email}),
        201  # Use HTTP status code 201 for resource created
    )

@app.route("/tms/<int:id>", methods=['PUT'])
def update_tm(id):
    data = request.get_json()
    tm = Tm.query.get(id)

    if not tm:
        return make_response(jsonify({'error': 'Tm not found'}), 404)

    # Update the Tm properties
    if 'Name' in data:
        tm.Name = data['Name']
    if 'Phone' in data:
        tm.Phone = data['Phone']
    if 'Email' in data:
        tm.Email = data['Email']

    db.session.commit()

    # Return the updated Tm record as a JSON response
    return make_response(jsonify({'id': tm.id, 'Name': tm.Name, 'Phone': tm.Phone, 'Email': tm.Email}), 200)

@app.route("/tms/<int:id>", methods=['DELETE'])
def delete_tm(id):
    tm = Tm.query.get(id)

    if not tm:
        return make_response(jsonify({'error': 'Tm not found'}), 404)

    db.session.delete(tm)
    db.session.commit()

    return jsonify({'message': 'Tm deleted successfully'})

if __name__ == '__main__':
    app.run(port=5555)

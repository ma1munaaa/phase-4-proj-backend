import os
from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from flask_cors import CORS


from models import Student,db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///checkin.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = '123456'  # Replace with a strong secret key




migrate = Migrate(app, db)

db.init_app(app)
# bcrypt = Bcrypt(app)



CORS(app)


# ... (previous code)



# Students

# Route to get all Student records
@app.route("/students", methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students])

# Route to create a new Student record
@app.route("/add-student", methods=['POST'])
def create_student():
    data = request.get_json()
    student = Student(Name=data.get('Name'), idnumber=data.get('idnumber'), phone=data.get('phone'), laptop_model=data.get('laptop_model'), serial_number=data.get('serial_number'), tm_name=data.get('tm_name'))
    db.session.add(student)
    db.session.commit()
    return make_response(
        jsonify({'id': student.id, 'Name': student.Name, 'idnumber': student.idnumber, 'phone': student.phone, 'laptop_model': student.laptop_model, 'serial_number': student.serial_number, 'tm_name': student.tm_name}),
        201  # Use HTTP status code 201 for resource created
    )

# Route to update an existing Student record by ID
@app.route("/students/<int:id>", methods=['PUT'])
def update_student(id):
    data = request.get_json()
    student = Student.query.get(id)

    if not student:
        return make_response(jsonify({'error': 'Student not found'}), 404)

    # Update the Student properties
    if 'Name' in data:
        student.Name = data['Name']
    if 'idnumber' in data:
        student.idnumber = data['idnumber']
    if 'phone' in data:
        student.phone = data['phone']
    if 'laptop_model' in data:
        student.laptop_model = data['laptop_model']
    if 'serial_number' in data:
        student.serial_number = data['serial_number']
    if 'tm_name' in data:
        student.tm_name = data['tm_name']

    db.session.commit()

    # Return the updated Student record as a JSON response
    return make_response(jsonify({'id': student.id, 'Name': student.Name, 'idnumber': student.idnumber, 'phone': student.phone, 'laptop_model': student.laptop_model, 'serial_number': student.serial_number, 'tm_name': student.tm_name}), 200)

# Route to delete an existing Student record by ID
@app.route("/students/<int:id>", methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)

    if not student:
        return make_response(jsonify({'error': 'Student not found'}), 404)

    db.session.delete(student)
    db.session.commit()

    return jsonify({'message': 'Student deleted successfully'})


if __name__ == '__main__':
    app.run(port=5555, debug=True)


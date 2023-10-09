from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Student(db.Model, SerializerMixin):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    idnumber = db.Column(db.String)  
    phone = db.Column(db.String)  
    laptop_model = db.Column(db.String)  
    serial_number = db.Column(db.String)  
    tm_name = db.Column(db.String)  

    def __repr__(self):
        return f'Student: {self.Name}, ID: {self.idnumber}, Phone: {self.phone}, Laptop Model: {self.laptop_model}, Serial Number: {self.serial_number}, TM: {self.tm_name}'

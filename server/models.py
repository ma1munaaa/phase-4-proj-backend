from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 113d40d3ccb9d68bc1c1bc97e3ecbed1c91f5c22
from datetime import datetime
import pytz


>>>>>>> 117fd24961ea022cfa48319f1d8cacdb4a20fe89

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
<<<<<<< HEAD
        return f'Student: {self.Name}, ID: {self.idnumber}, Phone: {self.phone}, Laptop Model: {self.laptop_model}, Serial Number: {self.serial_number}, TM: {self.tm_name}'
=======
        return f'CheckIn: {self.Name}, Room_number: {self.Room_number}, time_in: {self.time_in}'
    

<<<<<<< HEAD
=======
=======

db = SQLAlchemy()

class Tm(db.Model, SerializerMixin):
    __tablename__ = 'tm'
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    Phone = db.Column(db.String)
    Email = db.Column(db.String)

    def __repr__(self):
        return f'Tm: {self.Name}, Phone: {self.Phone}, Email: {self.Email}'
    
>>>>>>> 8291d26ef19d59061764119c092d8116b7982b71
>>>>>>> 113d40d3ccb9d68bc1c1bc97e3ecbed1c91f5c22
>>>>>>> 117fd24961ea022cfa48319f1d8cacdb4a20fe89

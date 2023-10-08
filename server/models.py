from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 113d40d3ccb9d68bc1c1bc97e3ecbed1c91f5c22
from datetime import datetime
import pytz



db = SQLAlchemy()

east_timezone = pytz.timezone('Africa/Nairobi')


class CheckIn(db.Model, SerializerMixin):
    __tablename__ = 'checkin'
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String) 
    Room_number = db.Column(db.Integer)  
    time_in = db.Column(db.DateTime, default=datetime.now(tz=east_timezone)) 

    def __repr__(self):
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

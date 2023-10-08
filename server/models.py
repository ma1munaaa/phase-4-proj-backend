from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Tm(db.Model, SerializerMixin):
    __tablename__ = 'tm'
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    Phone = db.Column(db.String)
    Email = db.Column(db.String)

    def __repr__(self):
        return f'Tm: {self.Name}, Phone: {self.Phone}, Email: {self.Email}'
    
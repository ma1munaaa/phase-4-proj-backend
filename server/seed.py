# seed.py
from app import db, Student, CheckIn, Tm, User
from faker import Faker

fake = Faker()

# Sample data for CheckIn
checkin_data = [
    {'Name': 'Eric Muthui', 'Room_number': 101},
    {'Name': 'Joyce Washira', 'Room_number': 102},
    {'Name': 'Ian Imbuki', 'Room_number': 103},
    {'Name': 'Maimuna Mohamud', 'Room_number': 106}
]

def seed_checkins():
    for data in checkin_data:
        name = data['Name']
        room_number = data['Room_number']
        new_checkin = CheckIn(Name=name, Room_number=room_number)
        db.session.add(new_checkin)
    db.session.commit()

student_data = [
    {
        'Name': 'Eric Muthui',
        'idnumber': '12345',
        'phone': '555-555-5555',
        'laptop_model': 'Macbook Pro',
        'serial_number': 'MBP12345',
        'tm_name': 'Teacher A',
    },
    {
        'Name': 'Joyce Washira',
        'idnumber': '54321',
        'phone': '555-555-1234',
        'laptop_model': 'Dell XPS',
        'serial_number': 'DXPS54321',
        'tm_name': 'Teacher B',
    },
    {
        'Name': 'Ian Imbuki',
        'idnumber': '67890',
        'phone': '555-555-6789',
        'laptop_model': 'HP Spectre',
        'serial_number': 'HPS67890',
        'tm_name': 'Teacher C',
    },
    {
        'Name': 'Maimuna Mohamud',
        'idnumber': '24680',
        'phone': '555-555-2468',
        'laptop_model': 'Lenovo ThinkPad',
        'serial_number': 'LT24680',
        'tm_name': 'Teacher D',
    },
]

def seed_students():
    for data in student_data:
        student = Student(**data)
        db.session.add(student)
    db.session.commit()

# Sample data for Tm
tm_data = [
    {
        'Name': 'TM One',
        'Phone': '555-555-5555',
        'Email': 'tm1@example.com',
    },
    {
        'Name': 'TM Two',
        'Phone': '555-555-1234',
        'Email': 'tm2@example.com',
    },
]

def seed_tms():
    for data in tm_data:
        tm = Tm(**data)
        db.session.add(tm)
    db.session.commit()

if __name__ == '__main__':
    from app import app

    with app.app_context():
        db.create_all()
        seed_checkins()
        seed_students()
        seed_tms()
        print('Database seeded successfully.')

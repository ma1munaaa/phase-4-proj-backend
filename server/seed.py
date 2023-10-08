<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 113d40d3ccb9d68bc1c1bc97e3ecbed1c91f5c22
from app import db, CheckIn
from faker import Faker

fake = Faker()

checkin_data = [
    {'Name': 'Eric Muthui', 'Room_number': 101},
    {'Name': 'Joyce Wahira', 'Room_number': 102},
    {'Name': 'Ian Imbuki', 'Room_number': 103},
    {'Name': 'Maimuna Mohamud', 'Room_number': 106}
]

def seed_database():
    for checkin_info in checkin_data:
        name = checkin_info['Name']
        room_number = checkin_info['Room_number']
        new_checkin = CheckIn(Name=name, Room_number=room_number)
        db.session.add(new_checkin)
    db.session.commit()

<<<<<<< HEAD
=======

>>>>>>> 113d40d3ccb9d68bc1c1bc97e3ecbed1c91f5c22
if __name__ == '__main__':
    from app import app

    with app.app_context():
        db.create_all()
        seed_database()
        print('Database seeded successfully.')



<<<<<<< HEAD
from app import db, Student
from faker import Faker

fake = Faker()

sample_students = [
        {
            'Name': 'John Doe',
            'idnumber': '12345',
            'phone': '555-555-5555',
            'laptop_model': 'Macbook Pro',
            'serial_number': 'MBP12345',
            'tm_name': 'Teacher A',
        },
        {
            'Name': 'Jane Smith',
            'idnumber': '54321',
            'phone': '555-555-1234',
            'laptop_model': 'Dell XPS',
            'serial_number': 'DXPS54321',
            'tm_name': 'Teacher B',
        },
    ]

def seed_database():
    for checkin_info in checkin_data:
        name = checkin_info['Name']
        room_number = checkin_info['Room_number']
        new_checkin = CheckIn(Name=name, Room_number=room_number)
        db.session.add(new_checkin)
    db.session.commit()

if __name__ == '__main__':
    from app import app

    with app.app_context():
        db.create_all()
        seed_database()
        print('Database seeded successfully.')





=======


=======
from app import app, db  # Assuming your Flask app instance and db object are defined in app.py
from models import Tm  # Import the Tm model class

def seed_database():
    # Sample data to seed the Tm table
    tm_data = [
        {"Name": "John Doe", "Phone": "123-456-7890", "Email": "john@example.com"},
        {"Name": "Jane Smith", "Phone": "987-654-3210", "Email": "jane@example.com"}
        # Add more data as needed
    ]

    # Seed the Tm table with the sample data
    for data in tm_data:
        name = data["Name"]
        phone = data["Phone"]
        email = data["Email"]
        tm_entry = Tm(Name=name, Phone=phone, Email=email)
        db.session.add(tm_entry)

    # Commit the changes to the database
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        # Call the seed_database function to populate the Tm table
        seed_database()
        print("Database seeded successfully!")
>>>>>>> 8291d26ef19d59061764119c092d8116b7982b71
>>>>>>> 113d40d3ccb9d68bc1c1bc97e3ecbed1c91f5c22

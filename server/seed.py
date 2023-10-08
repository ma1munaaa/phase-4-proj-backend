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


if __name__ == '__main__':
    from app import app

    with app.app_context():
        db.create_all()
        seed_database()
        print('Database seeded successfully.')






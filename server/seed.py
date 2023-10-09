from app import db, Student
from faker import Faker

fake = Faker()

student_data = [
    {
        'Name': 'Eric Muthui',
        'idnumber': '12345',
        'phone': '1234567890',
        'laptop_model': 'Dell XPS 13',
        'serial_number': 'ABC123',
        'tm_name': 'John Doe'
    },
    {
        'Name': 'Joyce Wahira',
        'idnumber': '54321',
        'phone': '9876543210',
        'laptop_model': 'MacBook Pro',
        'serial_number': 'XYZ789',
        'tm_name': 'Jane Smith'
    },
    {
        'Name': 'Ian Imbuki',
        'idnumber': '67890',
        'phone': '5555555555',
        'laptop_model': 'HP Spectre',
        'serial_number': 'DEF456',
        'tm_name': 'Robert Johnson'
    }
]

def seed_students():
    for student_info in student_data:
        name = student_info['Name']
        idnumber = student_info['idnumber']
        phone = student_info['phone']
        laptop_model = student_info['laptop_model']
        serial_number = student_info['serial_number']
        tm_name = student_info['tm_name']
        
        new_student = Student(
            Name=name,
            idnumber=idnumber,
            phone=phone,
            laptop_model=laptop_model,
            serial_number=serial_number,
            tm_name=tm_name
        )
        
        db.session.add(new_student)
    
    db.session.commit()

if __name__ == '__main__':
    from app import app

    with app.app_context():
        db.create_all()
        seed_students()
        print('Students table seeded successfully.')
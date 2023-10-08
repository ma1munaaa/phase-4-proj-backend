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

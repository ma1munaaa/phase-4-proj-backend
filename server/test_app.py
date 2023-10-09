import pytest
from app import app, db, CheckIn

@pytest.fixture
def client():
    """Create a test client for the app."""
    app.config['TESTING'] = True
    client = app.test_client()

    db.create_all()

    yield client

    db.drop_all()

def test_get_checkins(client):
    """Test the GET /checkins route."""
    checkin = CheckIn(Name="John Doe", Room_number="101")
    db.session.add(checkin)
    db.session.commit()

    response = client.get('/checkins')

    assert response.status_code == 200
    assert b"John Doe" in response.data
    assert b"101" in response.data

def test_create_checkin(client):
    """Test the POST /checkins route."""
    data = {
        "Name": "Jane Smith",
        "Room_number": "102"
    }

    response = client.post('/checkins', json=data)

    assert response.status_code == 201
    assert b"Jane Smith" in response.data
    assert b"102" in response.data

def test_update_checkin(client):
    """Test the PATCH /checkins/<id> route."""
    checkin = CheckIn(Name="Alice Johnson", Room_number="103")
    db.session.add(checkin)
    db.session.commit()

    data = {
        "Name": "Updated Name",
        "Room_number": "Updated Room"
    }

    response = client.patch(f'/checkins/{checkin.id}', json=data)

    assert response.status_code == 200

    updated_checkin = CheckIn.query.get(checkin.id)

    assert updated_checkin.Name == "Updated Name"
    assert updated_checkin.Room_number == "Updated Room"

def test_delete_checkin(client):
    """Test the DELETE /checkins/<id> route."""
    checkin = CheckIn(Name="Delete Me", Room_number="104")
    db.session.add(checkin)
    db.session.commit()

    response = client.delete(f'/checkins/{checkin.id}')

    assert response.status_code == 204

    deleted_checkin = CheckIn.query.get(checkin.id)

    assert deleted_checkin is None


if __name__ == '__main__':
    pytest.main()



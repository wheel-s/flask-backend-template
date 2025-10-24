import pytest
from app import create_app
from app.extensions import db
from flask_jwt_extended import decode_token



@pytest.fixture()
def client():
    app = create_app()
    #app.config.update({
        #"TESTING": True,
        #"SQLALCHEMY_DATABASE_URI":"sqlite:///:memory:"
    #})

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()






def test_user_reg(client):
    response = client.post("/api/auth/register", json={
        "username": "john",
        "email":"Cuzan2002@gmai.com",
        "password":"SECRET123",
        "role":"student"
    })

    assert response.status_code ==201
    assert b"john" in response.data


def jet(client):
    res = client.post('/api/auth/login', json={
        "email":"cuzan2002@gmail.com",
        "password":"brasam"
    })
    token = res.get_json()["access_token"]
    return token

def protected(client):
    token = jet()
    headers = {"Authorization": f"Bearer {token}"}
    res = client.get('/api/v1/students', headers)

    assert res.status_code ==200
    assert "email" in res.get_json()
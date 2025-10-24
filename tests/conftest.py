import pytest


from app import create_app
from app.extensions import db
from app.extensions import jwt

@pytest.fixture()
def  app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI":"sqlite:///:memory:",
        "JWT_SECRET_KEY":"test-secret",
        

    })

    with app.app_context():
        jwt.init_app(app)
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture()
def  client(app):
    return app.test_client()

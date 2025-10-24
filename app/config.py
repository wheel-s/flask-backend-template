import os
from datetime import timedelta

from dotenv import load_dotenv
load_dotenv()


class Config:
    JWT_SECRET_KEY = "test-secret"
    SQLALCHEMY_DATABASE_URI= "sqlite:///test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)
    JWT_VERIFY_SUB = False
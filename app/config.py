import os
from datetime import timedelta

from dotenv import load_dotenv
load_dotenv()


class Config:
    SECRET_KEY = "supersecret"
    JWT_SECRET_KEY = "test-secret"
    SQLALCHEMY_DATABASE_URI= "sqlite:///db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=3)
    JWT_VERIFY_SUB = False
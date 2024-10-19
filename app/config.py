import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/user_db")
    SECRET_KEY = os.getenv("SECRET_KEY", "thistopcoridersecret")

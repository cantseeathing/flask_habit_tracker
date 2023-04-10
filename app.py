import os

from flask import Flask
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


# GIT BASH FLASK_APP=app.py FLASK_DEBUG=true flask run
def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages)
    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.tracker
    print(app.db)
    return app

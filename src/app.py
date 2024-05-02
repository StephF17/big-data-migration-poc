import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from .config import configure_logger

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("SQLALCHEMY_DATABASE_URI")
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'REST API Service for RDS PostgreSQL'

# Run the Flask application
if __name__=='__main__':
    app.run()

configure_logger(app)

import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
load_dotenv()

# SQLALCHEMY_BINDS = {}
# SECRET_KEY = os.getenv('SECRET_KEY')

def configure_logger(app):
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs', 'app.log')
    file_handler = RotatingFileHandler(log_file_path, maxBytes=1024 * 1024, backupCount=10)
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)

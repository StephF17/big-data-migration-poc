import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def create_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv('LOCALHOST'),
            port=os.getenv('DB_PORT'),
            dbname=os.getenv('DB_DATABASE'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PWD'),
        )
        print("Database connected successfully.")
        return conn
    except psycopg2.OperationalError as oe:
        print("Error connecting database")
        raise oe


def close_connection(conn):
    if conn:
        conn.close()
        print("Connection closed.")

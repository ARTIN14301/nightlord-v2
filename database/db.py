import sqlite3
from database.schema import create_tables

DB_NAME = "nightlord.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    create_tables(cursor)

    conn.commit()
    conn.close()

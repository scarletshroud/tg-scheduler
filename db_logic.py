import sqlite3

db_connection = sqlite3.connect("scheduler.db")
db_cursor = db_connection.cursor()

def db_init():
    db_cursor.execute("""
                    CREATE TABLE user
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    name TEXT, 
                    surname TEXT,
                    slots INTEGER
                    reminder INTEGER
                    )
                    """)

    db_cursor.execute("""
                    CREATE TABLE slot
                    (
                    id INTEGER PRIMARY KEY  AUTOINCREMENT,
                    type TEXT, 
                    start_time TEXT,
                    end_time TEXT, 
                    status TEXT
                    )
                    """)
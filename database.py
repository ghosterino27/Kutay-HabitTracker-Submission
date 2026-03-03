import sqlite3

def connect_db(name="habits.db"):
    """Creates and returns a database connection."""
    return sqlite3.connect(name)

def initialize_tables():
    """Sets up the tables for habits and their completion logs."""
    conn = connect_db()
    cursor = conn.cursor()
    
    # Table to store habit definitions
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            periodicity TEXT NOT NULL
        )
    """)
    
    # Table to store when a habit was 'checked off' (Event Log)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS completions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_id INTEGER,
            timestamp TEXT NOT NULL,
            FOREIGN KEY (habit_id) REFERENCES habits (id)
        )
    """)
    conn.commit()
    conn.close()
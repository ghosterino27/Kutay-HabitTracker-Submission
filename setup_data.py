import database
from habit import Habit
from datetime import datetime, timedelta

def setup():
    # 1. Initialize the database and tables
    database.initialize_tables()
    conn = database.connect_db()
    
    # 2. Define 5 predefined habits (Requirement: "5 predefined habits")
    # We create a list of habits with their names and periodicities
    habits_to_create = [
        ("Gym", "daily"),
        ("Reading", "daily"),
        ("Project Work", "daily"),
        ("Car Wash", "weekly"),
        ("House Cleaning", "weekly")
    ]
    
    for name, period in habits_to_create:
        h = Habit(name, period)
        h.save()
    
    print("Successfully created 5 predefined habits.")

    # 3. Inject 4 weeks (28 days) of dummy data (Requirement: "4 weeks of example data")
    # This simulates a user checking off habits every day for a month.
    for habit_id in range(1, 6):  # For each of our 5 habits
        for i in range(28):      # For 28 days back from today
            # Create a unique timestamp for each day
            completion_date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d %H:%M:%S")
            cur = conn.cursor()
            cur.execute("INSERT INTO completions (habit_id, timestamp) VALUES (?, ?)", (habit_id, completion_date))
    
    conn.commit()
    conn.close()
    print("Successfully injected 4 weeks of tracking data for testing.")

if __name__ == "__main__":
    setup()
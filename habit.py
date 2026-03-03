from datetime import datetime
import database

class Habit:
    def __init__(self, name, periodicity):
        """Constructor for a habit object."""
        self.name = name
        self.periodicity = periodicity # 'daily' or 'weekly'

    def save(self):
        """Saves a new habit definition to the database."""
        conn = database.connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO habits (name, periodicity) VALUES (?, ?)", 
                       (self.name, self.periodicity))
        conn.commit()
        conn.close()

    @staticmethod
    def check_off(habit_id):
        """Records a completion event for a specific habit."""
        conn = database.connect_db()
        cursor = conn.cursor()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO completions (habit_id, timestamp) VALUES (?, ?)", 
                       (habit_id, now))
        conn.commit()
        conn.close()
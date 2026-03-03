import database
from datetime import datetime

def get_all_habits():
    """Fetches all habits from the database."""
    conn = database.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM habits")
    data = cursor.fetchall()
    conn.close()
    return data

def get_habits_by_period(periodicity):
    """Functional Programming: Filters habits by daily/weekly using lambda."""
    all_habits = get_all_habits()
    return list(filter(lambda h: h[2] == periodicity, all_habits))

def get_completions(habit_id):
    """Fetches all completion timestamps for a specific habit."""
    conn = database.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp FROM completions WHERE habit_id = ?", (habit_id,))
    data = [row[0] for row in cursor.fetchall()]
    conn.close()
    return data

def calculate_streak(habit_id):
    """Calculates the longest consecutive daily streak for a habit."""
    dates_str = get_completions(habit_id)
    if not dates_str:
        return 0

    # Convert strings to date objects and sort them
    dates = sorted(list(set([datetime.strptime(d, "%Y-%m-%d %H:%M:%S").date() for d in dates_str])))
    
    longest_streak = 0
    current_streak = 1
    
    if len(dates) == 1:
        return 1

    for i in range(len(dates) - 1):
        # Check if the next completion is exactly the next day
        if (dates[i+1] - dates[i]).days == 1:
            current_streak += 1
        else:
            longest_streak = max(longest_streak, current_streak)
            current_streak = 1
            
    return max(longest_streak, current_streak)
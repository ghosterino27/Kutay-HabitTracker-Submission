import pytest
import database
import analytics
from habit import Habit

# This runs before the tests to ensure we have a clean database
def setup_module(module):
    database.initialize_tables()

def test_habit_creation():
    """Test if a habit can be successfully created and saved."""
    test_habit = Habit("Test Gym", "daily")
    test_habit.save()
    
    all_habits = analytics.get_all_habits()
    # Check if 'Test Gym' exists in the database
    names = [h[1] for h in all_habits]
    assert "Test Gym" in names

def test_habit_periodicity():
    """Test if the functional filtering for daily habits works."""
    daily_habits = analytics.get_habits_by_period("daily")
    for h in daily_habits:
        assert h[2] == "daily"

def test_streak_calculation_empty():
    """Test if the streak is 0 for a new habit with no completions."""
    # Habit ID 999 doesn't exist, so streak should be 0
    streak = analytics.calculate_streak(999)
    assert streak == 0
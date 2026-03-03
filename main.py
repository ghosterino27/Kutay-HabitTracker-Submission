import database
import analytics
from habit import Habit

def main_menu():
    # Initializes the database tables on startup
    database.initialize_tables()
    print("--- Welcome to Habit Tracker ---")
    
    while True:
        print("\n1. Create New Habit")
        print("2. Check-off Habit (Mark as Complete)")
        print("3. List All Habits & Longest Streaks")
        print("4. Filter Habits by Periodicity")
        print("5. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            name = input("Enter habit name: ")
            period = input("Enter period (daily/weekly): ")
            new_habit = Habit(name, period)
            new_habit.save()
            print(f"Success: Habit '{name}' has been saved.")
            
        elif choice == "2":
            habits = analytics.get_all_habits()
            for h in habits:
                print(f"ID: {h[0]} | Name: {h[1]}")
            try:
                h_id = int(input("Enter the ID of the habit to check off: "))
                Habit.check_off(h_id)
                print("Success: Habit checked off!")
            except ValueError:
                print("Error: Please enter a valid numerical ID.")

        elif choice == "3":
            # This part uses the analytics module to calculate streaks
            habits = analytics.get_all_habits()
            print("\n--- Your Habits & Longest Streaks ---")
            for h in habits:
                streak = analytics.calculate_streak(h[0])
                print(f"ID: {h[0]} | Name: {h[1]} | Period: {h[2]} | Longest Streak: {streak} days")
                
        elif choice == "4":
            period = input("Enter period to filter by (daily/weekly): ")
            filtered = analytics.get_habits_by_period(period)
            print(f"\n--- {period.capitalize()} Habits ---")
            for h in filtered:
                print(f"Name: {h[1]}")

        elif choice == "5":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main_menu()
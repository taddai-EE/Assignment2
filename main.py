"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----


def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    semester_cost = annual_cost / SEMESTERS_PER_YEAR
    return semester_cost


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    month_cost = annual_cost / MONTHS_PER_YEAR
    return month_cost


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    day_cost = annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)
    return day_cost


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    
    credit_cost = cost_per_semester(annual_cost) / credits
    return credit_cost


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    class_cost = (cost_per_credit(annual_cost, credits) * CS1430_CREDITS) / CS1430_MEETINGS_PER_SEMESTER
    return class_cost

def cost_of_skipped_classes(annual_cost, credits, classes_skipped):
    """Give back the total cost of skipped classes this semester."""
    skipped_cost = cost_per_class(annual_cost, credits) * classes_skipped
    return skipped_cost
# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.print("Enter the total cost for one year:")
    annual_cost = float(input("Enter the total cost for one year: "))
    # Then ask for the credits this semester.
    credits = int(input("Enter the number of credits this semester: "))
    
    
    while True:
        # Show your menu here.
        print("Menu:")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per class day")
        print("4. Cost per credit")
        print("5. Cost per CS 1430 class")
        print("6. Cost of skipped classes")
        print("Q. Quit")
        
        choice = (input("Choose an option from the menu above: "))
        
        
        if choice == "Q":
            break
        elif choice == "1":
            print(f"One semester costs ${cost_per_semester(annual_cost):,.2f}")
        elif choice == "2":
            print(f"One month costs ${cost_per_month(annual_cost):,.2f}")
        elif choice == "3":
            print(f"One class day costs ${cost_per_day(annual_cost):,.2f}")
        elif choice == "4":
            print(f"One credit costs ${cost_per_credit(annual_cost, credits):,.2f}")
        elif choice == "5":
            print(f"One CS 1430 class costs ${cost_per_class(annual_cost, credits):,.2f}")
        elif choice == "6":
            classes_skipped = int(input("Enter the number of classes skipped this semester: "))
            print(f"The cost of skipped classes is "
                f"The cost of skipped classes is ${cost_of_skipped_classes(annual_cost, credits, classes_skipped):,.2f}")
        # Add a branch for each menu option here.
        else:
            print("Invalid choice. Please try again.")

# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()

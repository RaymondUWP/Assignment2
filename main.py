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
    credit_cost = annual_cost / (SEMESTERS_PER_YEAR * credits)
    return credit_cost


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    class_cost = ((annual_cost / (SEMESTERS_PER_YEAR * credits)) * CS1430_CREDITS) / CS1430_MEETINGS_PER_SEMESTER
    return class_cost

def cost_per_four_years(annual_cost):
    four_year_cost = (annual_cost * 4) + ((annual_cost * 4) * 0.2)
    return four_year_cost


# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    cost = float(input("Total Cost for One Year: "))

    # Then ask for the credits this semester.
    credits = float(input("Credits for this Semester: "))


    while True:
        print("1: Coster Per Semester")
        print("2: Coster Per Month")
        print("3: Coster Per Day")
        print("4: Coster Per Credit")
        print("5: Coster Per Class")
        print("6: Coster Per Four Years")

        choice = input("Choose an option: ")

        if choice == "Q":
            print("Thanks for running the numbers!")
            break
        elif choice == "1":
            print(f"One semester cost ${cost_per_semester(cost):.2f}")
        elif choice == "2":
            print(f"One month cost ${cost_per_month(cost):.2f}")
        elif choice == "3":
            print(f"One day cost ${cost_per_day(cost):.2f}")
        elif choice == "4":
            print(f"One credit cost ${cost_per_credit(cost, credits):.2f}")
        elif choice == "5": 
            print(f"One class cost ${cost_per_class(cost, credits):.2f}")
        elif choice == "6":
            print(f"Four year cost: ${cost_per_four_years(cost):.2f}")

        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()

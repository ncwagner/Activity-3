# Name: Noah Wagner
# Class: ISQA 3900-850
# Date: 9/5/2020
# Description: This program is a simple grade calculator. It obtains input from the user, and assigns a letter grade based on the total score.

def display_title():
    # Displays the title of the program when called.
    print("Welcome to the Grade Calculator")


def get_totalPoints(total_points):
    # This function prompts the user for and reads the total points earned.
    return total_points


def get_letterGrade(averageEarned):
    # This functions receives the average grade from the main() and returns the letter grade based on the average
    # earned.
    letter_Grade = ""
    if 92.0 <= averageEarned <= 100.0:
        letter_Grade = "A"
    elif 88.8 <= averageEarned <= 91.9:
        letter_Grade = "B+"
    elif 82.0 <= averageEarned <= 88.7:
        letter_Grade = "B"
    elif 78.0 <= averageEarned <= 81.9:
        letter_Grade = "C+"
    elif 70.0 <= averageEarned <= 77.8:
        letter_Grade = "C"
    elif 60.0 <= averageEarned <= 69.9:
        letter_Grade = "D"
    elif averageEarned < 60.0:
        letter_Grade = 'F'

    return letter_Grade


def main():

    display_title()
    print()

    choice = 'y'
    while choice.lower() == "y":

        bool_variable = True
        while bool_variable:
            total_points = int(input("Enter the total score (0-1000): "))
            if 0 <= total_points <= 1000:
                get_totalPoints(total_points)
                averageEarned = float(total_points / 1000 * 100)
                formatted_float = "{:.1f}".format(averageEarned)
                str_output = "You earned an average of " + formatted_float + "%. Letter grade earned: " + get_letterGrade(
                    averageEarned)
                print(str_output)
                print()
                choice = input("Would you like to enter another score (y/n)? ")
                print()
                bool_variable = False
            else:
                print("You must enter integer values >= 0 and <= 1000. Try again.")
                print()


if __name__ == "__main__":
    main()

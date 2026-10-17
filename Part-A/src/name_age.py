The purpose of this program is to ask what the name and age of someone is in order to get their birth year.
Input:
    The first input I will name as user_input. This will be used to ask the person what their name is 
    The secon input I will name as user_input2. This will be used to ask the person what their age is

Process:
    I will name the process birth_year and I will get it by subtracting their age from the current year
Output:
    I will use the print feature to greet the person, say their name, and then tell them what year they were born in.
Typical usage example:
    What is your name? John
    How old are you? 33
    Hello John! You were born in 1993.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    user_input = input("What is your name?")
    user_input2 = int(input("How old are you?"))

    # Calculate user's approximate birth year.
    birth_year = current_year - user_input2

    # Output personalized message with user's name and birth year.
    print("Hello", user_input, "! You were born in", birth_year,:.")


# === Main Guard ===
if __name__ == "__main__":
    main()



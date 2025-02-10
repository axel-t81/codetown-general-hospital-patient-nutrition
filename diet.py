#!/usr/bin/env python3
"""
This module takes patient nutrional info from hospital staff.
It then calculates the average protein, carbohydrates, fat, and kilojoules for all patients.
"""
# Program Details
__author__ = "Axel Tracy"
__version__ = "0.1.15"


# Initialise empty Lists for each nutritional macro
# Use Lists as they allow duplicates, are changeable, and are iterable and can be worked on
all_protein = []
all_carbs = []
all_fat = []
all_kjs = []

# Initialise global variables used in program
justify = " "
line = "*"

# A function to collect valid input for nutritional macro data.
# This function validates input to confirm (a) it is a number that fits the requirements of a float, and (b) that it is non-negative.
# For citing sources, this function is from learning from StackOverflow.
# My original StackOverflow question was asked here: https://stackoverflow.com/questions/78814504/in-python-why-is-this-negative-float-passing-the-non-negative-while-loop-test-c
# And not only did @Andrew Yim answer my original question, he pointed me to a StackFlow guide on how to better tackle this input validation problem.
# The guide he pointed me to was here: https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
# For learning quickly about Try and Except, this guide was used: https://www.youtube.com/watch?v=MImAiZIzzd4
def non_negative_only(prompt):
    """Validate patient number input."""
    while True:
        try:
            value = float(input(prompt))
        except:
            print("\nSorry, I didn't understand your input. Let's try again, using a whole number or one with decimal places, as your input please.")
            continue

        if value < 0:
            print("\nSorry, the amount must be a non-negative number. Please try again.")
            continue
        else:
            break
    return value

# A function to collect valid input for patients numbers.
# This function validates input to confirm (a) it is an integer to count people, and (b) that it is positive and above zero.
def positive_int_only(prompt):
    """Validate the nutritional macro input."""
    while True:
        try:
            value = int(input(prompt))
        except:
            print("\nSorry, I didn't understand your input. Let's try again, using a whole number to count people, as your input please.")
            continue

        if value < 1:
            print("\nSorry, the number of patients must be a positive number. Please try again.")
            continue
        else:
            break
    return value

# A function to format the averages output.
# The idea and template here was drawn from my submission to the Week 3 Assessable Tutorial, the 'Right Justify' problem.
# In short, there are three scenarios to this selection statement;
# 1) A standard number that is 12 digits or less, which should cover all cases in regards to the current nutrition use case,
# 2) A alternative option if there an extremely large number with 13 to 30 digits, which should be highly unlikely.
# 3) A final catch-all case, to tie up any number that isn't covered by the last two options.
def right_align(input_string):
    """Calculate the length of the input string and align string to the right."""
    info = input_string
    characters = len(info)
    if characters <= 12:
        blanks = 12 - characters
        return (blanks*justify + info)
    elif (12 < characters <= 30):
        blanks = 30 - characters
        return (blanks*justify + info)
    else:
        return info

# The main function; guarded by the diet.py script entry point below.
def main():
    """Main entry point of program."""
    # For UI and user-friendliness, provide feedback to user of program start/entry point.
    print("\n" + line*100)
    print("WELCOME TO THE CODETOWN GENERAL HOSPITAL PATIENT NUTRITION SYSTEM:")
    print(line*100 + "\n")

    # Requirement 1: "request the number of patient's dietary requirements that will be entered in the interaction with the program"
    # This uses the function above to return an integer to the variable
    patients = positive_int_only("\nHow many patients are you collecting data for, today? ")

    # For UI and user-friendliness, provide feedback and guidance to user of where they are in the program.
    print("\n\nSTEP 1 of 2 - PATIENT NUTRITION COLLECTION:")

    # Requirement 2: "loop this number of times to collect the amount of protein, carbohydrates, and fat required for each patient."
    # Using range() allows the for loop to be interable over an int, and solved an error message previously received
    for x in range(patients):
        # For UI and user-friendliness, when describing patient to user, add 1 to zero-based index and typecast int x to string
        # This String variable is used in the prompts below.
        x_string = str(x + 1)

        # This uses the function above to return an float to the variable
        protein = non_negative_only("\nHow many grams of protein is required for patient " + x_string + "? ")
        # Append most recent float input to end of appropriate List.
        all_protein.append(protein)

        carbs = non_negative_only("\nHow many grams of carbohydrates are required for patient " + x_string + "? ")
        all_carbs.append(carbs)

        fat = non_negative_only("\nHow many grams of fat is required for patient " + x_string + "? ")
        all_fat.append(fat)

        # Calculate Kjs for each patient, and add it to the appropriate List
        kilojoules_unrounded = (4.18 * (4 * protein + 4 * carbs + 9.30 * fat))
        # Using the round() function to handle complex float; 
        # Setting precision to 4 to not lose data within calculations, even though the output is later formatted to 2 decinal places
        kilojoules = round(kilojoules_unrounded, 4)
        all_kjs.append(kilojoules)

    # Calculate and Output Averages of All Four Lists
    print("\n\nSTEP 2 of 2 - CALCULATED PATIENT INFORMATION:\n")

    # Calculating the average by summing List items to get a total for numerator; and using len() function to count items to use as denominator
    # This is rounded to two decimal places to improve UI and user experience
    protein_average_float = round(sum(all_protein) / len(all_protein),2)
    # 1) Using the right_align function decribed earlier
    # 2) Typecasting the float, the average, to a string so it can be used in string concatination
    # 3) Using the f-string capabilities of Python to format the output to 2 decimal places
    protein_average = right_align(str(f'{protein_average_float:.2f}'))
    # The justify variable is used here by manually calculating the length of string to left and hardcoding into string; the goal of this is to have all strings of the average calculations in line with each other.
    # Achieving this goals allow easier recognigtion of the size of each number, e.g. 1000 should be easily distinguishable vs 100.
    print("Protein - The average protein over all patients is:" + justify*13 + protein_average + " grams")

    carbs_average_float = round(sum(all_carbs) / len(all_carbs),2)
    carbs_average = right_align(str(f'{carbs_average_float:.2f}'))
    print("Carbohydrates - The average carbohydrates over all patients is:" + justify*1 + carbs_average + " grams")

    fat_average_float = round(sum(all_fat) / len(all_fat),2)
    fat_average = right_align(str(f'{fat_average_float:.2f}'))
    print("Fat - The average fat over all patients is:" + justify*21 + fat_average + " grams")

    kjs_average_float = round(sum(all_kjs) / len(all_kjs),2)
    kjs_average = right_align(str(f'{kjs_average_float:.2f}'))
    print("Kilojoules - The average kilojoules over all patients is:" + justify*7 + kjs_average + " kJs\n")

    # Final out to provide feedback to user, and confirm the program is complete, and they can safely shut down.
    print("\n" + line*100)
    print("THE SYSTEM IS NOW COMPLETE: YOUR PATIENTS' NUTRITIONAL INFORMATION IS NOW AVAILABLE FOR USE.\nPLEASE CLOSE THIS PROGRAM OR RUN AGAIN. THANK YOU.")
    print(line*100 + "\n")


# This is the entry point of the diet.py program/script.
# This code in this conditional statement runs when executed as a script from the command line; the file object passing to the interpreter evaluates as True.
# But this code will not run when functions are imported via a module; only the function would be used externally.
if __name__ == "__main__":
    """This is executed when run as a script from the command line."""
    main()


# References:
# * https://www.python-boilerplate.com/py3+executable - For boilerplate code to start with.
# * https://www.w3schools.com/python/ - Guidance on using in-built Python functions.
# * https://www.geeksforgeeks.org/ - Guidance on using in-built Python functions.
# * https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places - Guidance to learn about f-strings.
# * https://chatgpt.com/c/89aff71f-f728-4fdb-96c1-9e5930a845a6 - Guidance to find out why my original input validation had false negative errors in testing.
# * https://realpython.com/if-name-main-python/ - Guidance to learn about the if-name-main conditional statement, and why programs are set up this way.
# * https://www.britannica.com/topic/large-numbers-1765137 - Guidance when working out how to setup the right_align function.
# * https://packaging.python.org/en/latest/guides/making-a-pypi-friendly-readme/ - For guidance with the README.md file
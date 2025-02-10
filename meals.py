#!/usr/bin/env python3
"""
This module takes patient nutrional info from hospital staff.
It then determines the best diet to provide to the patient, as per standardised dietary guidelines.
It then prints the diet selection to a csv file, for persistency.
"""
# Program Details
__author__ = "Axel Tracy"
__version__ = "0.1.9"

# Import Statements
import math 
import os

# Initialise global variables and dictionaries used in program
cwd = os.getcwd()
line = "*"
normal_diet = {
    "protein": 32.5,
    "carbohydrates": 60.0,
    "fat": 40.86
}
oncology_diet = {
    "protein": 35.0,
    "carbohydrates": 52.5,
    "fat": 37.63
}
cardiology_diet = {
    "protein": 32.5,
    "carbohydrates": 30.0,
    "fat": 26.88
}
diabetes_diet = {
    "protein": 20.0,
    "carbohydrates": 27.5,
    "fat": 27.95
}
kidney_diet = {
    "protein": 15.0,
    "carbohydrates": 55.0,
    "fat": 23.65
}

# Since I didn't get the full Patient ID Validation working, this function was my workaround
# This function confirms the Patient ID is a valid integer, and is a positive, non-negative number
def valid_patient_id(prompt):
    """Validate Patient ID input."""
    while True:
        try:
            patient_id = int(input(prompt))
        except:
            print("\nSorry, I didn't understand your input. Let's try again, using numbers for your Patient ID, as your input please.")
            continue
        if patient_id < 1:
            print("\nSorry, the Patient ID must be a positive number. Please try again.")
            continue
        else:
            break
    return patient_id

# A function to collect valid input for nutritional macro data.
# This function validates input to confirm (a) it is a number that fits the requirements of a float, and (b) that it is non-negative.
def non_negative_only(prompt):
    """Validate nutritional data input."""
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

# A function to calculate the error of the nutrional requirements versus the standardised diets.
# The function takes set, initialised dictionary, the dictionary created in choose_diet() function, and calculates the error
def calculate_error(diet, requirements):
    """From the entered dietary requirements, calculate the absolute value errors against all standard diets"""
    pro_diet = diet["protein"]
    pro_req = requirements["protein"]
    pro_error = abs(pro_diet - pro_req)

    carb_diet = diet["carbohydrates"]
    carb_req = requirements["carbohydrates"]
    carb_error = abs(carb_diet - carb_req)

    fat_diet = diet["fat"]
    fat_req = requirements["fat"]
    fat_error = abs(fat_diet - fat_req)

    total_error = (pro_error + carb_error + fat_error)

    return total_error

# A function to choose which diet is best.
# The function takes user input and builds a dictionary with it
# Then it walks over the calculate_error function, to determine the error against all set diets, placing these errors in a dictionary too
# Then from within the error dictionary, it determines the key (i.e. diet) with the minimum error
# It prints out this minimum error diet and returns it for use in the meals.csv file writing.
# It then 
def choose_diet(protein, carbohydrates, fat):
    """Chooses diet with the lowest absolute value error."""
    patient_diet = {
        "protein": protein,
        "carbohydrates" : carbohydrates,
        "fat": fat
        }
    error_dict = {}
    error_dict["Normal"] = calculate_error(normal_diet, patient_diet)
    error_dict["Oncology"] = calculate_error(oncology_diet, patient_diet)
    error_dict["Cardiology"] = calculate_error(cardiology_diet, patient_diet)
    error_dict["Diabetes"] = calculate_error(diabetes_diet, patient_diet)
    error_dict["Kidney"] = calculate_error(kidney_diet, patient_diet)

    min_error = min(error_dict.values())

    key_list = list(error_dict.keys())
    val_list = list(error_dict.values())
    lowest_error_diet = val_list.index(min_error)
    lowest_error_diet_key = (key_list[lowest_error_diet])
    print(f"\nThe best diet, with the lowest error rate is, for the patient is the {lowest_error_diet_key} diet.")

    return lowest_error_diet_key


# The main function; guarded by the meals.py script entry point below.
def main():
    """Main entry point of program."""
    # For UI and user-friendliness, provide feedback to user of program start/entry point.
    print("\n" + line*100)
    print("WELCOME TO THE CODETOWN GENERAL HOSPITAL NUTRITION-BASED DIET SELECTION SYSTEM:")
    print(line*100 + "\n")

    # Requirement 1: "Your program should start by asking for the patient id (which is a six-digit positive integer with no leading zeroes)"
    # This uses the function above to return a six-digit integer to the variable
    patient_id = valid_patient_id("\nPlease enter the Patient ID: ")

    # For UI and user-friendliness, provide feedback and guidance to user of where they are in the program.
    print("\n\nPATIENT NUTRITION COLLECTION:")

    # Requirement 2: "your program must ask for the amount of protein, carbohydrates, and fat required by that patient (which must all be non-negative numbers)."

    # This uses the function above to return an float to the variable
    # The variables are then used as parameters below in the choose_diet() function
    protein = non_negative_only(f"\nHow many grams of protein is required for the patient with ID {patient_id} ? ")
    carbohydrates = non_negative_only(f"\nHow many grams of carbohydrates are required for the patient with ID {patient_id}? ")
    fat = non_negative_only(f"\nHow many grams of fat is required for the patient with ID {patient_id}? ")

    # This use of choose_diet() stores the selected diet (with min error) in a variable to use for file writing
    diet_data = choose_diet(protein, carbohydrates, fat)

    # Using the f string, we create the string that will be written to the meals.csv file
    file_contents = f"{patient_id},{diet_data}\n"

    # We create the csv file here
    with open(os.path.join(cwd, 'meals.csv'), 'a') as file:
        file.write(file_contents)

    # Final out to provide feedback to user, and confirm the program is complete, and they can safely shut down.
    print("\n" + line*100)
    print("THE SYSTEM IS NOW COMPLETE: YOUR PATIENTS' NUTRITION-BASED DIET SELECTIONS HAVE BEEN MADE.\nTHESE DIETS HAVE BEEN SENT TO THE KITCHEN VIA A CSV FILE.\nPLEASE CLOSE THIS PROGRAM OR RUN AGAIN. THANK YOU.")
    print(line*100 + "\n")

    # Note: I was unable to implement the option to keep looping the Patient IDs until a blank was entered.
    # Thus: The program is limited to one Patient for execution. Apologies for this.


# This is the entry point of the meals.py program/script.
# This code in this conditional statement runs when executed as a script from the command line; the file object passing to the interpreter evaluates as True.
# But this code will not run when functions are imported via a module; only the function would be used externally.
if __name__ == "__main__":
    """This is executed when run as a script from the command line."""
    main()





# References:
# * https://www.w3schools.com/python/ - Guidance on using in-built Python functions.
# * https://www.geeksforgeeks.org/ - Guidance on using in-built Python functions.
# * https://stackoverflow.com/questions/2189800/how-to-find-length-of-digits-in-an-integer
# * https://www.w3schools.com/python/ref_math_log10.asp
# * https://www.tutorialspoint.com/python/number_log10.htm
# * https://www.geeksforgeeks.org/find-first-last-digits-number/
# * https://www.jeremymorgan.com/python/how-to-get-first-character-of-a-string-in-python/
# * https://www.w3schools.com/PYTHON/python_dictionaries_add.asp
# * https://www.geeksforgeeks.org/python-minimum-value-keys-in-dictionary/
# * https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/
# * https://www.geeksforgeeks.org/create-an-empty-file-using-python/
# * https://www.geeksforgeeks.org/create-a-new-text-file-in-python/
# * https://www.w3schools.com/python/python_file_write.asp
# * https://stackoverflow.com/questions/4288973/whats-the-difference-between-s-and-d-in-string-formatting
# * https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
# * https://www.geeksforgeeks.org/g-fact-41-multiple-return-values-in-python/=

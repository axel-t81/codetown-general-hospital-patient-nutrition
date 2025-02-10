#!/usr/bin/env python3
"""
This module takes allows users to select one of the standardised diets.
When that diet is selected, the amount of protein, carbohydrates, fat, and kilojoules is displayed.
All of this is done within a GUI.
"""
# Program Details
__author__ = "Axel Tracy"
__version__ = "0.1.13"


# Add required import statements
from tkinter import *
from tkinter import ttk


# Initialise Dictionaries with Standardised Diets
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


# Calculate Kjs for each diet, that will be displayed
# The function has protein, carbohydrates, and fat as arguments
def calc_kjs(pr, ca, fa):
    """Calculates kJs of each diet, to diplay."""
    # The kJ calculation formula from Programming Task 1
    kilojoules_unrounded = (4.18 * (4 * pr + 4 * ca + 9.30 * fa))
    # Using the round() function to handle complex float; 
    # Setting precision 2 decimal places
    kilojoules_var = round(kilojoules_unrounded, 2)
    return kilojoules_var

# While it was originally hoped ome function could minimise the code below, by differentiating which diet was clicked,
# in the end the priority was to get the task working, and the five functions below became the final version.

# A function to be called when Normal Diet is required via command
def click_normal(*args):
    """Displays Normal Diet data in GUI"""
    # Set the DoubleVars
    kilojoules.set(f'{calc_kjs(normal_diet["protein"], normal_diet["carbohydrates"], normal_diet["fat"]):.2f}')
    protein.set(f'{normal_diet["protein"]:.2f}')
    carbohydrates.set(f'{normal_diet["carbohydrates"]:.2f}')
    fat.set(f'{normal_diet["fat"]:.2f}')
    # Create the labels for the DoubleVars and one StringVar
    selected_diet_label_var = ttk.Label(frame, text = "Normal", anchor = "e")
    protein_label_var = ttk.Label(frame, width = 12, textvariable = protein, anchor = "e")
    carbohydrates_label_var = ttk.Label(frame, width = 12, textvariable = carbohydrates, anchor = "e")
    fat_label_var = ttk.Label(frame, width = 12, textvariable = fat, anchor = "e")
    kilojoules_label_var = ttk.Label(frame, width = 12, textvariable = kilojoules, anchor = "e")
    # Display the label for the DoubleVars and one StringVar
    selected_diet_label_var.grid(column = 4, row = 3, sticky = (N, S, E, W))
    protein_label_var.grid(column = 4, row = 4, sticky = (N, S, E, W))
    carbohydrates_label_var.grid(column = 4, row = 5, sticky = (N, S, E, W))
    fat_label_var.grid(column = 4, row = 6, sticky = (N, S, E, W))
    kilojoules_label_var.grid(column = 4, row = 7, sticky = (N, S, E, W))

# A function to be called when Oncology Diet is required via command
def click_oncology(*args):
    """Displays Oncology Diet data in GUI"""
    # Set the DoubleVars
    kilojoules.set(f'{calc_kjs(oncology_diet["protein"], oncology_diet["carbohydrates"], oncology_diet["fat"]):.2f}')
    protein.set(f'{oncology_diet["protein"]:.2f}')
    carbohydrates.set(f'{oncology_diet["carbohydrates"]:.2f}')
    fat.set(f'{oncology_diet["fat"]:.2f}')
    # Create the labels for the DoubleVars and one StringVar
    selected_diet_label_var = ttk.Label(frame, text = "Oncology", anchor = "e")
    protein_label_var = ttk.Label(frame, width = 12, textvariable = protein, anchor = "e")
    carbohydrates_label_var = ttk.Label(frame, width = 12, textvariable = carbohydrates, anchor = "e")
    fat_label_var = ttk.Label(frame, width = 12, textvariable = fat, anchor = "e")
    kilojoules_label_var = ttk.Label(frame, width = 12, textvariable = kilojoules, anchor = "e")
    # Display the label for the DoubleVars and one StringVar
    selected_diet_label_var.grid(column = 4, row = 3, sticky = (N, S, E, W))
    protein_label_var.grid(column = 4, row = 4, sticky = (N, S, E, W))
    carbohydrates_label_var.grid(column = 4, row = 5, sticky = (N, S, E, W))
    fat_label_var.grid(column = 4, row = 6, sticky = (N, S, E, W))
    kilojoules_label_var.grid(column = 4, row = 7, sticky = (N, S, E, W))

# A function to be called when Cardiology Diet is required via command
def click_cardiology(*args):
    """Displays Cardiology Diet data in GUI"""
    # Set the DoubleVars
    kilojoules.set(f'{calc_kjs(cardiology_diet["protein"], cardiology_diet["carbohydrates"], cardiology_diet["fat"]):.2f}')
    protein.set(f'{cardiology_diet["protein"]:.2f}')
    carbohydrates.set(f'{cardiology_diet["carbohydrates"]:.2f}')
    fat.set(f'{cardiology_diet["fat"]:.2f}')
    # Create the labels for the DoubleVars and one StringVar
    selected_diet_label_var = ttk.Label(frame, text = "Cardiology", anchor = "e")
    protein_label_var = ttk.Label(frame, width = 12, textvariable = protein, anchor = "e")
    carbohydrates_label_var = ttk.Label(frame, width = 12, textvariable = carbohydrates, anchor = "e")
    fat_label_var = ttk.Label(frame, width = 12, textvariable = fat, anchor = "e")
    kilojoules_label_var = ttk.Label(frame, width = 12, textvariable = kilojoules, anchor = "e")
    # Display the label for the DoubleVars and one StringVar
    selected_diet_label_var.grid(column = 4, row = 3, sticky = (N, S, E, W))
    protein_label_var.grid(column = 4, row = 4, sticky = (N, S, E, W))
    carbohydrates_label_var.grid(column = 4, row = 5, sticky = (N, S, E, W))
    fat_label_var.grid(column = 4, row = 6, sticky = (N, S, E, W))
    kilojoules_label_var.grid(column = 4, row = 7, sticky = (N, S, E, W))

# A function to be called when Diabetes Diet is required via command
def click_diabetes(*args):
    """Displays Diabetes Diet data in GUI"""
    # Set the DoubleVars
    kilojoules.set(f'{calc_kjs(diabetes_diet["protein"], diabetes_diet["carbohydrates"], diabetes_diet["fat"]):.2f}')
    protein.set(f'{diabetes_diet["protein"]:.2f}')
    carbohydrates.set(f'{diabetes_diet["carbohydrates"]:.2f}')
    fat.set(f'{diabetes_diet["fat"]:.2f}')
    # Create the labels for the DoubleVars and one StringVar
    selected_diet_label_var = ttk.Label(frame, text = "Diabetes", anchor = "e")
    protein_label_var = ttk.Label(frame, width = 12, textvariable = protein, anchor = "e")
    carbohydrates_label_var = ttk.Label(frame, width = 12, textvariable = carbohydrates, anchor = "e")
    fat_label_var = ttk.Label(frame, width = 12, textvariable = fat, anchor = "e")
    kilojoules_label_var = ttk.Label(frame, width = 12, textvariable = kilojoules, anchor = "e")
    # Display the label for the DoubleVars and one StringVar
    selected_diet_label_var.grid(column = 4, row = 3, sticky = (N, S, E, W))
    protein_label_var.grid(column = 4, row = 4, sticky = (N, S, E, W))
    carbohydrates_label_var.grid(column = 4, row = 5, sticky = (N, S, E, W))
    fat_label_var.grid(column = 4, row = 6, sticky = (N, S, E, W))
    kilojoules_label_var.grid(column = 4, row = 7, sticky = (N, S, E, W))

# A function to be called when Kidney Diet is required via command
def click_kidney(*args):
    """Displays Kidney Diet data in GUI"""
    # Set the DoubleVars
    kilojoules.set(f'{calc_kjs(kidney_diet["protein"], kidney_diet["carbohydrates"], kidney_diet["fat"]):.2f}')
    protein.set(f'{kidney_diet["protein"]:.2f}')
    carbohydrates.set(f'{kidney_diet["carbohydrates"]:.2f}')
    fat.set(f'{kidney_diet["fat"]:.2f}')
    # Create the labels for the DoubleVars and one StringVar
    selected_diet_label_var = ttk.Label(frame, text = "Kidney", anchor = "e")
    protein_label_var = ttk.Label(frame, width = 12, textvariable = protein, anchor = "e")
    carbohydrates_label_var = ttk.Label(frame, width = 12, textvariable = carbohydrates, anchor = "e")
    fat_label_var = ttk.Label(frame, width = 12, textvariable = fat, anchor = "e")
    kilojoules_label_var = ttk.Label(frame, width = 12, textvariable = kilojoules, anchor = "e")
    # Display the label for the DoubleVars and one StringVar
    selected_diet_label_var.grid(column = 4, row = 3, sticky = (N, S, E, W))
    protein_label_var.grid(column = 4, row = 4, sticky = (N, S, E, W))
    carbohydrates_label_var.grid(column = 4, row = 7, sticky = (N, S, E, W))
    fat_label_var.grid(column = 4, row = 6, sticky = (N, S, E, W))
    kilojoules_label_var.grid(column = 4, row = 7, sticky = (N, S, E, W))


# Create the root of the hierarchy
root = Tk()

# Set default window size
root.geometry("1000x500")

# Give the GUI window a Title
root.title("Codetown Hospital: Diet Information")

# Create the frame of the window
frame = ttk.Frame(root, padding = (3, 3, 12, 12), borderwidth = 5, relief = "sunken")

# Configure the frame to cover the root window and make it sticky to all sides
frame.grid(column=0, row=0, sticky=(N,S,E,W))

# Two for loops to configure rows and columns of the grid and set each row and coloumn to a weight of 1
# Code to enable resizing, on the cells, rows, and columns
for i in range(1, 8):
    frame.rowconfigure(i, weight=1)

for i in range(1, 6):
    frame.columnconfigure(i, weight=1)


# Create the labels for static text
selected_diet_label = ttk.Label(frame, text = "Selected Diet:", anchor = "e", borderwidth = 2, relief="ridge", padding = "5")
protein_label = ttk.Label(frame, text = "Protein (g):", anchor = "e", borderwidth = 2, relief="ridge", padding = "5")
carbohydrates_label = ttk.Label(frame, text = "Cabohydrates (g):", anchor = "e", borderwidth = 2, relief="ridge", padding = "5")
fat_label = ttk.Label(frame, text = "Fat (g):", anchor = "e", borderwidth = 2, relief="ridge", padding = "5")
kilojoules_label = ttk.Label(frame, text = "Kilojoules (kJs):", anchor = "e", borderwidth = 2, relief="ridge", padding = "5")
select_diet_label = ttk.Label(frame, text = "Select the Diet Option to Display:", anchor = "center", borderwidth = 2, relief="ridge", padding = "5")

# Display the labels for static text
selected_diet_label.grid(column = 2, row = 3, sticky = (N, S, E, W))
protein_label.grid(column = 2, row = 4, sticky = (N, S, E, W))
carbohydrates_label.grid(column = 2, row = 5, sticky = (N, S, E, W))
fat_label.grid(column = 2, row = 6, sticky = (N, S, E, W))
kilojoules_label.grid(column = 2, row = 7, sticky = (N, S, E, W))
select_diet_label.grid(column = 1, row = 1, columnspan = 5, sticky = ((N, S, E, W)))


# Create the Buttons for each Diet
normal_button = ttk.Button(frame, width = 8, text = "Normal", command = click_normal)
oncology_button = ttk.Button(frame, width = 8, text = "Oncology", command = click_oncology)
cardiology_button = ttk.Button(frame, width = 8, text = "Cardiology", command = click_cardiology)	
diabetes_button = ttk.Button(frame, width = 8, text = "Diabetes", command = click_diabetes)	
kidney_button = ttk.Button(frame, width = 8, text = "Kidney", command = click_kidney)		

# Display Buttons for each Diet
normal_button.grid(column = 1, row = 2, sticky = (N, W, E, S))
oncology_button.grid(column = 2, row = 2, sticky=(N, S, E, W))
cardiology_button.grid(column = 3, row = 2, sticky = (N, S, E, W))
diabetes_button.grid(column = 4, row = 2, sticky = (N, S, E, W))
kidney_button.grid(column = 5, row = 2, sticky = (N, S, E, W))


# Create the DoubleVars that will be set in the functions above
protein = DoubleVar(frame)
carbohydrates = DoubleVar(frame)
fat = DoubleVar(frame)
kilojoules = DoubleVar(frame)

# Code to set padding of the cells and window
for child in frame.winfo_children():			
    child.grid_configure(padx = 3, pady = 3)

# Code to enable resizing, on the root itself
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Code required so GUI waits for events, and script doesn't just start, run, end/close in blink of eye
root.mainloop()


# References:
# * https://www.w3schools.com/python/
# * https://www.geeksforgeeks.org/
# * https://www.geeksforgeeks.org/python-passing-dictionary-as-arguments-to-function/
# * https://www.geeksforgeeks.org/python-passing-dictionary-as-keyword-arguments/
# * https://www.reddit.com/r/Python/comments/jp0x4d/taking_a_dictionary_as_an_argument_is_the_root_of/
# * https://blog.furas.pl/python-tkinter-how-to-set-size-for-empty-row-or-column-in-grid-gb.html"
# * https://stackoverflow.com/questions/75250679/tkinter-making-a-large-number-of-cells-with-grid-while-using-geometry-property
# * https://www.reddit.com/r/Tkinter/comments/19ay94h/why_wont_tkinter_resize_my_image/
# * https://pythonroadmap.com/blog/tkinter-grid-manager-tutorial#spanning-rows-and-columns	
# * https://stackoverflow.com/questions/40767893/how-to-center-a-label-in-a-tkinter-colspan-using-grid
# * https://stackoverflow.com/questions/25328787/can-you-pack-multiple-tkinter-widgets-at-a-time-rather-than-packing-them-individ
# * https://www.tutorialspoint.com/how-can-i-resize-the-root-window-in-tkinter
# * https://stackoverflow.com/questions/30923448/what-does-the-00-in-geometry-mean-in-tkinter
# * https://stackoverflow.com/questions/21766890/python-tkinter-frame-and-canvas-will-expand-horizontally-but-not-vertically-w					
# * https://stackoverflow.com/questions/7591294/how-to-create-a-self-resizing-grid-of-buttons-in-tkinter	
# * https://www.geeksforgeeks.org/how-to-align-text-in-tkinter-label/
# * https://stackoverflow.com/questions/31140590/how-to-line-left-justify-label-and-entry-boxes-in-tkinter-grid			
# * https://www.w3schools.com/python/python_dictionaries_access.asp
# * https://stackoverflow.com/questions/45310254/fixed-digits-after-decimal-with-f-strings
# * https://www.geeksforgeeks.org/dynamically-resize-buttons-when-resizing-a-window-using-tkinter/
# * https://stackoverflow.com/questions/68109119/how-can-i-set-default-screen-tkinter-not-full-screen
# * https://chatgpt.com/c/66eae6c5-e980-800c-b5bf-3120f9f97fbe
#       ChatGPT Qustion Flow 1: "Why is my tkinter sticky attribute not working? It will stretch E and W for a Button, but not N and S?"			
#       ChatGPT Qustion Flow 2: "If I try Option 1, where in my file should I place that code?"	
#       ChatGPT Qustion Flow 3: "That Option didn't work, do you have any other ideas what's occuring?"			
#       ChatGPT Qustion Flow 4: "Does running this code on a Mac have any effect on the tkinter Buttons?"			
# codetown-general-hospital-patient-nutrition

## Description
A Python-based patient nutrition system for hospital staff. The three different programs of this repo formed the programming assignments for UNE's COSC110.

## The Three Programs

### *1. Patient Nutrion Needs System*

This small, shell-based, Python program was an individual programming task for COSC110 at the University of New England (UNE).

While the exact requirements of the program remain the IP of UNE, the aim of the program is as following:
* Allow a hospital staff member to enter the nutrional needs of their patients.
* They do this by first entering the number of patients they are responsible for.
* They then enter the nutrional needs of each individual patient, i.e. the optimal daily protein, carbohydrates, and fat.
* Once all patient macronutrient needs have been entered, the program will:

  | Calculation | Output |
  | ----------- | ------ |
  | 1 | Average macronutrient levels across all patients (for procurement and meal planning reasons) |
  | 2 | Average kilojoules (kJs) across all patients (for medical and health reasons) |

* The program will then close.

Instructions to use the program:

1. Open shell (e.g. bash, zshell, etc)
2. Change directory (cd command) to location where tgz file was extracted.
3. (Optional) Confirm diet.py is in directory with ls command.
4. Run program via the following command
   4.1 For Python 3 machines: python3 diet.py
   4.2 For machines with earlier Python versions: python diet.py
5. (Optional) To close program prior to completion of script, simply close shell

Instructions to access the README.md in shell:

1. Open shell (e.g. bash, zshell, etc)
2. Change directory (cd command) to location where tgz file was extracted.
3. (Optional) Confirm README.md is in directory with ls command.
4. Run and Open README.md via the following command
   4.1 For Python 3 machines: pydoc3 ./diet.py
   4.2 For machines with earlier Python versions: pydoc diet.py
   
---

### *2. Diet Selection System*

This small, shell-based, Python program was an individual programming task for COSC110 at the University of New England (UNE).

While the exact requirements of the program remain the IP of UNE, the aim of the program is as following:
* Allows a hospital staff member choose the best standardised diet for a patient, based on the patient's nutrional needs. I.e. To choose among the available diets already within the hospital, that themselves have been set by international guidelines on what is needed for different health conditions.
* Firstly, the patient is selected by the staff member, based on their Patient ID.
* The staff member then enters the individual nutrional needs of the patient, i.e. their optimal daily protein, carbohydrates, and fat.
* Based on these individual needs, the program then runs a function over the internationally-provided diet guidelines. It finds which of the six set diets has the lowest absolute value error against the patient's individual dietary needs. This allows the system to select the best standardised diet that is available in the hospital.
* After selecting the best diet, the program performs two (2) actions:
  
  | No. | Action |
  | ----------- | ------ |
  | 1 | It prints to the screen the selected diet for the patient, so the hospital staff member is aware |
  | 2 | It generates or adds to a CSV file that includes (a) Patient ID (b) Diet Selected, so the hospital kitchen can later be sent the CSV for meal planning and prep |

* The program will then close.

Instructions to use the program:

1. Open shell (e.g. bash, zshell, etc)
2. Change directory (cd command) to location where tgz file was extracted.
3. (Optional) Confirm meals.py is in directory with ls command.
4. Run program via the following command
   4.1 For Python 3 machines: python3 meals.py
   4.2 For machines with earlier Python versions: python meals.py
5. (Optional) To close program prior to completion of script
   5.1 Press Ctrl + Z on Unix systems

Instructions to access the README.md in shell:

1. Open shell (e.g. bash, zshell, etc)
2. Change directory (cd command) to location where tgz file was extracted.
3. (Optional) Confirm README.md is in directory with ls command.
4. Run and Open README.md via the following command
   4.1 For Python 3 machines: pydoc3 ./meals.py
   4.2 For machines with earlier Python versions: pydoc meals.py

---

### *3. Diet Information GUI*

This is a basic GUI using Python's Tkinter. It was the 3rd individual programming task for COSC110 at the University of New England (UNE).

While the exact requirements of the program remain the IP of UNE, the aim of the program is as following:
* See the nutrional information of each of the standardised diets available in the hospital.
* Selecting and viewing this information is done within a resizeable GUI.
* Hospital staff members can run the program and then use the GUI and it's buttons to select the different standardised diets.
* After a diet's button is clicked, the nutrional macros for that diet are diplayed, and the kilojoules (kJs) for that diet are calculated within the program and also diplayed.
* While this 3rd Codetown Hospital program is far simpler than the first two, ideally the GUI would make it more user-friendly for the hospital's staff to use.
   
Instructions to use the program:

1. Open shell (e.g. bash, zshell, etc)
2. Change directory (cd command) to location where tgz file was extracted.
3. (Optional) Confirm dietGUI.py is in directory with ls command.
4. Run program via the following command:
   4.1 For Python 3 machines: python3 dietGUI.py
   4.2 For machines with earlier Python versions: python dietGUI.py
5. Operate the Program by clicking on the Diet buttons in the GUI.
6. To close program:
   6.1 Click the standard 'Close' button in the GUI window
   6.2 Press Ctrl + Z on Unix systems, when in shell

Instructions to access the README.md in shell:

1. Open shell (e.g. bash, zshell, etc)
2. Change directory (cd command) to location where tgz file was extracted.
3. (Optional) Confirm README.md is in directory with ls command.
4. Run and Open README.md via the following command
   4.1 For Python 3 machines: pydoc3 ./dietGUI.py
   4.2 For machines with earlier Python versions: pydoc dietGUI.py

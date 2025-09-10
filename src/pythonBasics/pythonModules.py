"""
PYTHON MODULES - DEMONSTRATION SCRIPT
-------------------------------------
This script demonstrates:
1. Creating a custom module
2. Importing and using it
3. Module variables
4. Aliases with 'as'
5. Built-in modules
6. dir() function
7. Importing specific parts
"""

print("\n==============================")
print(" PYTHON MODULES - DEMO ")
print("==============================\n")

# ------------------------------------------------------
# STEP 1: CREATE A CUSTOM MODULE (mymodule.py)
# ------------------------------------------------------
# Save this as a separate file: mymodule.py
"""
# FILE: mymodule.py
def greeting(name):
    print("Hello,", name)

person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}
"""

print("1. Custom Module Created: mymodule.py")
print("   - Contains a function 'greeting(name)'")
print("   - Contains a dictionary 'person1'\n")

# ------------------------------------------------------
# STEP 2: IMPORT AND USE THE MODULE
# ------------------------------------------------------
import mymodule   # Import our custom module

print("2. Using Custom Module")
mymodule.greeting("Jonathan")   # Call function from module
print("Access dictionary from module:", mymodule.person1)
print("Age from dictionary:", mymodule.person1["age"], "\n")

# ------------------------------------------------------
# STEP 3: MODULE VARIABLES
# ------------------------------------------------------
print("3. Variables in Module")
print("The person1 dictionary from mymodule contains:")
for k, v in mymodule.person1.items():
    print(f"  {k}: {v}")
print("Important Note: A module can contain variables, arrays, dictionaries, functions, etc.\n")

# ------------------------------------------------------
# STEP 4: RENAME MODULE USING 'as'
# ------------------------------------------------------
import mymodule as mx   # alias

print("4. Aliasing a Module")
print("Accessing with alias 'mx':", mx.person1["age"])
print("Important Note: Aliases make code shorter and easier to type.\n")

# ------------------------------------------------------
# STEP 5: BUILT-IN MODULE (platform)
# ------------------------------------------------------
import platform

print("5. Built-in Module: platform")
print("System platform is:", platform.system())
print("Python version is:", platform.python_version())
print("Important Note: Python provides many built-in modules for system, math, OS, etc.\n")

# ------------------------------------------------------
# STEP 6: dir() FUNCTION
# ------------------------------------------------------
print("6. Using dir() on Modules")
print("List of attributes/methods in platform module:")
print(dir(platform)[:15])   # print first 15 items for brevity
print("Important Note: dir() helps us explore available functions/variables in a module.\n")

# ------------------------------------------------------
# STEP 7: IMPORT SPECIFIC PARTS FROM A MODULE
# ------------------------------------------------------
from mymodule import person1, greeting

print("7. Importing Specific Parts from a Module")
greeting("Alice")   # no need to use mymodule.greeting()
print("Directly accessing imported dictionary:", person1)
print("Person's country:", person1["country"], "\n")

print("==============================")
print(" END OF PYTHON MODULES DEMO ")
print("==============================")

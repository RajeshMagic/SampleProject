# -------------------------------------------
# Python Variables - Full Demonstration
# -------------------------------------------

print("========== PYTHON VARIABLES DEMO ==========\n")

# 1. Creating Variables
print("1. Creating Variables:")
x = 5
y = "John"
print("x =", x, "-> integer")
print("y =", y, "-> string\n")

# 2. Changing Type of a Variable
print("2. Changing Type of a Variable:")
x = 4       # int
print("Initially, x =", x, "-> type:", type(x))
x = "Sally" # now string
print("Now, x =", x, "-> type:", type(x), "\n")

# 3. Casting
print("3. Casting (forcing data types):")
x = str(3)    # '3'
y = int(3)    # 3
z = float(3)  # 3.0
print("x =", x, "->", type(x))
print("y =", y, "->", type(y))
print("z =", z, "->", type(z), "\n")

# 4. Getting Type
print("4. Getting Type with type():")
x = 5
y = "John"
print("Type of x =", type(x))
print("Type of y =", type(y), "\n")

# 5. Single or Double Quotes
print("5. Strings can use single or double quotes:")
x = "John"
print("x =", x)
x = 'John'
print("x =", x, "\n")

# 6. Case Sensitivity
print("6. Case-Sensitive Variables:")
a = 4
A = "Sally"
print("a =", a, "| A =", A, "\n")

# 7. Variable Names Rules
print("7. Variable Naming Rules:")
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print("Examples of legal variable names:")
print("myvar, my_var, _my_var, myVar, MYVAR, myvar2 -> All valid!\n")
print("Illegal examples would be: 2myvar, my-var, my var (won't run in Python)\n")

# 8. Multi-Word Variable Names
print("8. Multi-word Variable Naming Styles:")
myVariableName = "Camel Case"
MyVariableName = "Pascal Case"
my_variable_name = "Snake Case"
print("Camel Case:", myVariableName)
print("Pascal Case:", MyVariableName)
print("Snake Case:", my_variable_name, "\n")

# 9. Assign Multiple Values
print("9. Assigning Multiple Values at Once:")
x, y, z = "Orange", "Banana", "Cherry"
print("x =", x, "| y =", y, "| z =", z, "\n")

# 10. One Value to Multiple Variables
print("10. One Value to Multiple Variables:")
x = y = z = "Orange"
print("x =", x, "| y =", y, "| z =", z, "\n")

# 11. Unpack a Collection
print("11. Unpacking a Collection:")
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print("Unpacked -> x =", x, "| y =", y, "| z =", z, "\n")

# 12. Output Variables
print("12. Output Variables with print():")
x = "Python is awesome"
print(x)
x, y, z = "Python", "is", "awesome"
print("Using commas:", x, y, z)
print("Using + operator:", x + " " + y + " " + z)
print("For numbers, + is addition:")
print("5 + 10 =", 5 + 10)
print("Mixing types with + gives error, so use commas instead:")
x = 5
y = "John"
print("x =", x, ", y =", y, "\n")

# 13. Global Variables
print("13. Global Variables:")
x = "awesome"  # Global variable
def myfunc():
    print("Inside function: Python is " + x)

myfunc()
print("Outside function: Python is " + x, "\n")

# Local variable with same name
print("Local variable with same name as global:")
x = "awesome"

def myfunc2():
    x = "fantastic"  # Local variable
    print("Inside function:", x)

myfunc2()
print("Outside function:", x, "\n")

# Using global keyword
print("Using 'global' keyword to modify global variable:")

def myfunc3():
    global x
    x = "fantastic"

myfunc3()
print("After using global, x =", x, "\n")

print("========== END OF DEMO ==========")

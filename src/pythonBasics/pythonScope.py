"""
PYTHON SCOPE - DEMONSTRATION SCRIPT
------------------------------------
This program demonstrates the concept of variable scope in Python:
1. Local Scope
2. Function Inside Function (inner function accessing outer scope)
3. Global Scope
4. Local vs Global with same name
5. global keyword
6. nonlocal keyword
"""

print("\n==============================")
print(" PYTHON SCOPE - DEMONSTRATION ")
print("==============================\n")

# ------------------------------------------------------
# 1. LOCAL SCOPE
# ------------------------------------------------------
print("1. LOCAL SCOPE")
print("--------------")

def myfunc_local():
    x = 300   # Local variable
    print(f"Inside function, local x = {x}")

myfunc_local()
# print(x)  # ❌ This would cause an error: x is not defined here (local to function)

print("Important Note: Variables defined inside a function are LOCAL to that function.\n")


# ------------------------------------------------------
# 2. FUNCTION INSIDE FUNCTION
# ------------------------------------------------------
print("2. FUNCTION INSIDE FUNCTION")
print("---------------------------")

def myfunc_outer():
    x = 300   # Local to outer function
    def myfunc_inner():
        print(f"Inner function accessing outer x = {x}")
    myfunc_inner()

myfunc_outer()

print("Important Note: Inner functions can access variables from their enclosing (outer) function.\n")


# ------------------------------------------------------
# 3. GLOBAL SCOPE
# ------------------------------------------------------
print("3. GLOBAL SCOPE")
print("---------------")

x = 300  # Global variable

def myfunc_global():
    print(f"Inside function, accessing global x = {x}")

myfunc_global()
print(f"Outside function, global x = {x}")

print("Important Note: Variables defined outside functions are GLOBAL and accessible everywhere.\n")


# ------------------------------------------------------
# 4. NAMING VARIABLES (Local vs Global Conflict)
# ------------------------------------------------------
print("4. NAMING VARIABLES (Local vs Global Conflict)")
print("----------------------------------------------")

x = 300  # Global variable

def myfunc_conflict():
    x = 200   # Local variable with same name
    print(f"Inside function, local x = {x}")

myfunc_conflict()
print(f"Outside function, global x = {x}")

print("Important Note: Local and Global variables with the same name are treated as SEPARATE variables.\n")


# ------------------------------------------------------
# 5. GLOBAL KEYWORD
# ------------------------------------------------------
print("5. GLOBAL KEYWORD")
print("-----------------")

# Example A: Creating a global variable inside a function
def myfunc_create_global():
    global y   # declare y as global
    y = 400
    print(f"Inside function, created global y = {y}")

myfunc_create_global()
print(f"Outside function, global y = {y}")

# Example B: Modifying a global variable inside a function
z = 500
def myfunc_modify_global():
    global z
    z = 600
    print(f"Inside function, modified global z = {z}")

print(f"Before function call, global z = {z}")
myfunc_modify_global()
print(f"After function call, global z = {z}")

print("Important Note: Use 'global' keyword to CREATE or MODIFY a global variable from inside a function.\n")


# ------------------------------------------------------
# 6. NONLOCAL KEYWORD
# ------------------------------------------------------
print("6. NONLOCAL KEYWORD (Nested Functions)")
print("--------------------------------------")

def outer_function():
    msg = "Jane"   # variable in outer (enclosing) scope
    def inner_function():
        nonlocal msg   # declare msg refers to outer function's variable
        msg = "Hello"
    inner_function()
    return msg

result = outer_function()
print(f"After calling outer_function, msg = {result}")

print("Important Note: 'nonlocal' allows modifying variables in the OUTER (non-global) function scope.\n")


print("==============================")
print(" END OF PYTHON SCOPE DEMO ")
print("==============================")

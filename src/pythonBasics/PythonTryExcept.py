# ==============================================================
# PYTHON EXCEPTION HANDLING (TRY - EXCEPT - ELSE - FINALLY)
# ==============================================================
# Exception Handling is one of the most important features in Python.
# It allows us to handle errors gracefully without crashing the program.
#
# Key blocks:
#  - try     : Code that may cause an error
#  - except  : Code that runs if an error occurs
#  - else    : Runs if NO error occurs
#  - finally : Runs ALWAYS (used for cleanup, closing files, etc.)
# ==============================================================

print("\n==============================")
print(" 1. BASIC TRY - EXCEPT ")
print("==============================")

try:
    print(x)  # x is not defined
except:
    print("An exception occurred: Variable 'x' is not defined")

print("\n==============================")
print(" 2. WITHOUT TRY - PROGRAM CRASHES ")
print("==============================")
print("Important Note: Uncommenting the below line will crash program")
# print(x)   # Uncommenting this line will raise NameError and stop execution


print("\n==============================")
print(" 3. MULTIPLE EXCEPTIONS HANDLING ")
print("==============================")

try:
    print(x)  # Again 'x' not defined
except NameError:
    print("Handled NameError: Variable x is not defined")
except:
    print("Handled some other error")


print("\n==============================")
print(" 4. TRY - ELSE BLOCK ")
print("==============================")

try:
    print("Hello World!")  # No error here
except:
    print("Something went wrong")
else:
    print("Nothing went wrong (Else block executed)")


print("\n==============================")
print(" 5. TRY - FINALLY BLOCK ")
print("==============================")

try:
    print(y)  # y is not defined, will raise NameError
except:
    print("Exception caught in 'except' block")
finally:
    print("Finally block executed - cleanup code goes here")


print("\n==============================")
print(" 6. FILE HANDLING WITH TRY - EXCEPT - FINALLY ")
print("==============================")

try:
    f = open("demofile.txt")  # File exists but may not be writable
    try:
        f.write("Hello World")  # Will fail if opened in read mode
    except:
        print("Error: Something went wrong while writing to the file")
    finally:
        f.close()
        print("Finally block executed: File closed safely")
except:
    print("Error: Could not open the file")


print("\n==============================")
print(" 7. RAISING EXCEPTIONS MANUALLY ")
print("==============================")

x = -1
try:
    if x < 0:
        raise Exception("Custom Exception: Sorry, no numbers below zero")
except Exception as e:
    print("Exception Raised ->", e)


print("\n==============================")
print(" 8. RAISING SPECIFIC EXCEPTION (TypeError) ")
print("==============================")

x = "hello"
try:
    if not type(x) is int:
        raise TypeError("Only integers are allowed, but got string")
except TypeError as e:
    print("Exception Raised ->", e)


print("\n==============================")
print(" END OF DEMO ")
print("==============================")

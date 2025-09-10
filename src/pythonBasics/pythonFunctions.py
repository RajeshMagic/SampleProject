"""
==========================================
Python Functions - Comprehensive Examples
==========================================

This script demonstrates:
- Creating & calling functions
- Arguments (positional, keyword, *args, **kwargs)
- Default values
- Passing lists
- Return values
- The pass statement
- Positional-only & keyword-only arguments
- Recursion
"""

print("\n==========================")
print("1. Basic Function Example")
print("==========================")

def my_function():
    print("Hello from a function!")

# Calling the function
my_function()


print("\n==========================")
print("2. Function with Arguments")
print("==========================")

def greet_user(fname, lname):
    print(f"Hello {fname} {lname}!")

greet_user("Emil", "Refsnes")


print("\n==========================")
print("3. *args (Arbitrary Arguments)")
print("==========================")

def show_kids(*kids):
    print("The youngest child is:", kids[-1])

show_kids("Emil", "Tobias", "Linus")


print("\n==========================")
print("4. Keyword Arguments")
print("==========================")

def show_family(child1, child2, child3):
    print("The youngest child is:", child3)

show_family(child1="Emil", child2="Tobias", child3="Linus")


print("\n==========================")
print("5. **kwargs (Arbitrary Keyword Arguments)")
print("==========================")

def show_person(**person):
    print("Person details:", person)
    print("His last name is:", person["lname"])

show_person(fname="Tobias", lname="Refsnes", age=20)


print("\n==========================")
print("6. Default Parameter Value")
print("==========================")

def from_country(country="Norway"):
    print("I am from", country)

from_country("Sweden")
from_country("India")
from_country()  # Uses default value
from_country("Brazil")


print("\n==========================")
print("7. Passing a List as Argument")
print("==========================")

def print_food(food_list):
    print("Food list received inside function:")
    for item in food_list:
        print(" -", item)

fruits = ["apple", "banana", "cherry"]
print_food(fruits)


print("\n==========================")
print("8. Return Values")
print("==========================")

def multiply_by_five(x):
    return 5 * x

print("5 * 3 =", multiply_by_five(3))
print("5 * 5 =", multiply_by_five(5))
print("5 * 9 =", multiply_by_five(9))


print("\n==========================")
print("9. The pass Statement")
print("==========================")

def future_function():
    # Placeholder for future code
    pass

print("The function 'future_function' exists but does nothing (pass).")


print("\n==========================")
print("10. Positional-Only Arguments")
print("==========================")

def show_number(x, /):  # '/' means x must be positional
    print("Value of x is:", x)

show_number(3)
# show_number(x=3)  # This would cause an ERROR


print("\n==========================")
print("11. Keyword-Only Arguments")
print("==========================")

def display_value(*, x):  # '*' means x must be keyword-only
    print("Value of x is:", x)

display_value(x=10)
# display_value(10)  # This would cause an ERROR


print("\n==========================")
print("12. Combine Positional & Keyword-Only")
print("==========================")

def combined_example(a, b, /, *, c, d):
    print(f"a={a}, b={b}, c={c}, d={d}")
    print("Sum =", a + b + c + d)

combined_example(5, 6, c=7, d=8)


print("\n==========================")
print("13. Recursion Example")
print("==========================")

def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print("Intermediate result:", result)
    else:
        result = 0
    return result

print("Recursion Example Results:")
tri_recursion(6)

print("\n===================================")
print("All Function Concepts Demonstrated!")
print("===================================")

# ============================================================
# PYTHON CONTROL FLOW & LOOPING DEMO
# Covers: If-Else, Elif, Short-hand If, Match, While Loop,
# For Loop, Break, Continue, Else in Loops, Nested Loops,
# and Function (Method) examples
# ============================================================

print("\n==============================")
print("PYTHON CONDITIONS & IF STATEMENTS")
print("==============================")

# Basic If
a, b = 33, 200
print(f"\nExample 1: Compare a={a}, b={b}")
if b > a:
    print("✔ b is greater than a")

# Elif
a, b = 33, 33
print(f"\nExample 2: Compare a={a}, b={b}")
if b > a:
    print("✔ b is greater than a")
elif a == b:
    print("✔ a and b are equal")

# Else
a, b = 200, 33
print(f"\nExample 3: Compare a={a}, b={b}")
if b > a:
    print("✔ b is greater than a")
elif a == b:
    print("✔ a and b are equal")
else:
    print("✔ a is greater than b")

# Short-hand If and If-Else
a, b = 2, 330
print(f"\nExample 4: Short-hand If and If-Else (a={a}, b={b})")
print("✔ a > b") if a > b else print("✔ b >= a")

# Multiple Short-hand Else
a, b = 330, 330
print(f"\nExample 5: Multiple conditions inline (a={a}, b={b})")
print("✔ A") if a > b else print("✔ Equal") if a == b else print("✔ B")

# Logical Operators
a, b, c = 200, 33, 500
print(f"\nExample 6: Logical Operators (a={a}, b={b}, c={c})")
if a > b and c > a:
    print("✔ Both conditions are True")
if a > b or a > c:
    print("✔ At least one condition is True")
if not a < b:
    print("✔ a is NOT less than b")

# Nested If
x = 41
print(f"\nExample 7: Nested If (x={x})")
if x > 10:
    print("✔ Above 10")
    if x > 20:
        print("✔ and also above 20!")
    else:
        print("✔ but not above 20.")

# Pass Statement
print("\nExample 8: Pass Statement (No error with empty if)")
if b > a:
    pass

# ============================================================
print("\n==============================")
print("PYTHON MATCH STATEMENT (Python 3.10+)")
print("==============================")

day = 4
print(f"\nExample 9: Match Statement (day={day})")
match day:
    case 1:
        print("✔ Monday")
    case 2:
        print("✔ Tuesday")
    case 3:
        print("✔ Wednesday")
    case 4:
        print("✔ Thursday")
    case 5:
        print("✔ Friday")
    case 6:
        print("✔ Saturday")
    case 7:
        print("✔ Sunday")

# Default (underscore)
print("\nExample 10: Match with Default Case")
day = 9
match day:
    case 6:
        print("✔ Saturday")
    case 7:
        print("✔ Sunday")
    case _:
        print("✔ Not a valid day (default case)")

# Combine values
print("\nExample 11: Combine Values with | operator")
day = 6
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("✔ Weekday")
    case 6 | 7:
        print("✔ Weekend!")

# Guards
print("\nExample 12: Guards with if")
month, day = 5, 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("✔ A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("✔ A weekday in May")
    case _:
        print("✔ No match")

# ============================================================
print("\n==============================")
print("PYTHON WHILE LOOPS")
print("==============================")

i = 1
print("\nExample 13: Simple while loop")
while i < 6:
    print("✔ i =", i)
    i += 1

print("\nExample 14: Break in while loop")
i = 1
while i < 6:
    print("✔ i =", i)
    if i == 3:
        print("✔ Breaking loop at i=3")
        break
    i += 1

print("\nExample 15: Continue in while loop")
i = 0
while i < 6:
    i += 1
    if i == 3:
        print("✔ Skipping i=3")
        continue
    print("✔ i =", i)

print("\nExample 16: Else in while loop")
i = 1
while i < 4:
    print("✔ i =", i)
    i += 1
else:
    print("✔ Condition is no longer true, loop ended")

# ============================================================
print("\n==============================")
print("PYTHON FOR LOOPS")
print("==============================")

fruits = ["apple", "banana", "cherry"]
print("\nExample 17: Loop through list")
for f in fruits:
    print("✔ Fruit:", f)

print("\nExample 18: Loop through string 'banana'")
for c in "banana":
    print("✔ Char:", c)

print("\nExample 19: Break in for loop")
for f in fruits:
    if f == "banana":
        print("✔ Stopping at banana")
        break
    print("✔ Fruit:", f)

print("\nExample 20: Continue in for loop")
for f in fruits:
    if f == "banana":
        print("✔ Skipping banana")
        continue
    print("✔ Fruit:", f)

print("\nExample 21: Range function")
for x in range(2, 10, 3):
    print("✔ Number:", x)

print("\nExample 22: Else in for loop")
for x in range(3):
    print("✔ Number:", x)
else:
    print("✔ Loop ended naturally (no break)")

print("\nExample 23: Break prevents else")
for x in range(3):
    if x == 1:
        break
    print("✔ Number:", x)
else:
    print("✔ This will NOT run")

print("\nExample 24: Nested Loops")
adj = ["red", "big", "tasty"]
for a in adj:
    for f in fruits:
        print(f"✔ {a} {f}")

# ============================================================
print("\n==============================")
print("PYTHON FUNCTIONS (METHODS)")
print("==============================")

def greet(name="Guest"):
    """Simple greeting function"""
    return f"Hello, {name}!"

print("\nExample 25: Function with default argument")
print(greet())
print(greet("Alice"))

def add_numbers(a, b):
    """Return sum of two numbers"""
    return a + b

print("\nExample 26: Function with arguments and return value")
print("✔ 5 + 10 =", add_numbers(5, 10))

def factorial(n):
    """Recursive function to calculate factorial"""
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("\nExample 27: Recursive Function (Factorial)")
print("✔ 5! =", factorial(5))

def print_kwargs(**kwargs):
    """Function demonstrating keyword arguments"""
    for key, value in kwargs.items():
        print(f"✔ {key} = {value}")

print("\nExample 28: Function with keyword arguments")
print_kwargs(name="Bob", age=25, city="New York")

# ============================================================
print("\n==============================")
print("END OF DEMO")
print("==============================")

# -------------------------------------------
# Python Booleans - Full Demonstration
# -------------------------------------------

print("========== PYTHON BOOLEAN DEMO ==========\n")

# 1. Boolean Values from Comparisons
print("1. Boolean Values from Comparisons:")
print("10 > 9  ->", 10 > 9)
print("10 == 9 ->", 10 == 9)
print("10 < 9  ->", 10 < 9)
print()

# 2. Booleans in Conditions
print("2. Booleans in if Statements:")
a, b = 200, 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
print()

# 3. Using bool() to Evaluate Values
print("3. Evaluating Values with bool():")
print("bool('Hello') ->", bool("Hello"))
print("bool(15)      ->", bool(15))

x, y = "Hello", 15
print("bool(x) where x='Hello' ->", bool(x))
print("bool(y) where y=15      ->", bool(y))
print()

# 4. Most Values are True
print("4. Most Values are True if they have content:")
print("bool('abc')                   ->", bool("abc"))
print("bool(123)                     ->", bool(123))
print("bool(['apple','cherry','banana']) ->", bool(["apple", "cherry", "banana"]))
print()

# 5. Some Values are False
print("5. But some values are False (empty or zero):")
print("bool(False) ->", bool(False))
print("bool(None)  ->", bool(None))
print("bool(0)     ->", bool(0))
print("bool('')    ->", bool(""))
print("bool(())    ->", bool(()))
print("bool([])    ->", bool([]))
print("bool({})    ->", bool({}))
print()

# 6. Objects with __len__ returning 0 are False
print("6. Custom objects with __len__ returning 0 evaluate to False:")

class MyClass:
    def __len__(self):
        return 0

myobj = MyClass()
print("bool(myobj) ->", bool(myobj))
print()

# 7. Functions Returning Booleans
print("7. Functions that Return Boolean Values:")

def myFunction():
    return True

print("myFunction() ->", myFunction())

if myFunction():
    print("Since myFunction() is True, print YES!")
else:
    print("Since myFunction() is False, print NO!")
print()

# 8. Built-in Functions Returning Boolean
print("8. Built-in Functions that Return Booleans:")
x = 200
print("isinstance(x, int) ->", isinstance(x, int))
print("isinstance(x, str) ->", isinstance(x, str))
print()

print("========== END OF BOOLEAN DEMO ==========")

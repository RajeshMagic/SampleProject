# ==============================
# PYTHON TUPLES - DEMONSTRATION
# ==============================

print("\n--- 1. Creating Tuples ---")
# A tuple is an ordered, unchangeable collection
tuple1 = ("apple", "banana", "cherry")
print("Tuple:", tuple1)

# Allowing duplicates
tuple2 = ("apple", "banana", "cherry", "apple", "cherry")
print("Tuple with duplicates:", tuple2)

# Tuple length
print("Length of tuple1:", len(tuple1))

# One-item tuple
one_item = ("apple",)
not_tuple = ("apple")
print("One item tuple:", one_item, "-> type:", type(one_item))
print("Not a tuple:", not_tuple, "-> type:", type(not_tuple))

# Tuples with different data types
mixed_tuple = ("abc", 34, True, 40, "male")
print("Mixed tuple:", mixed_tuple)

# Using tuple() constructor
constructed = tuple(("apple", "banana", "cherry"))
print("Tuple created using constructor:", constructed)

# ----------------------------
print("\n--- 2. Accessing Tuple Items ---")
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("Original tuple:", thistuple)
print("Item at index 1:", thistuple[1])
print("Last item (index -1):", thistuple[-1])
print("Slice [2:5] -> items from index 2 to 4:", thistuple[2:5])
print("Slice [:4] -> first 4 items:", thistuple[:4])
print("Slice [2:] -> from index 2 to end:", thistuple[2:])
print("Negative slice [-4:-1] -> last 4th to last 2nd:", thistuple[-4:-1])

# Check if item exists
if "apple" in thistuple:
    print("'apple' is present in tuple")

# ----------------------------
print("\n--- 3. Updating Tuples (Workarounds) ---")
x = ("apple", "banana", "cherry")
print("Original tuple:", x)

# Change item (convert to list, modify, back to tuple)
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print("After modifying second item:", x)

# Add item (list conversion)
y = list(x)
y.append("orange")
x = tuple(y)
print("After adding 'orange':", x)

# Add item using tuple concatenation
z = ("mango",)
x += z
print("After concatenating another tuple:", x)

# Remove item workaround
y = list(x)
y.remove("apple")
x = tuple(y)
print("After removing 'apple':", x)

# Delete entire tuple
del x
print("Tuple deleted with del (cannot print now).")

# ----------------------------
print("\n--- 4. Unpacking Tuples ---")
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print("Unpacked:", green, yellow, red)

fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits2
print("Using * -> green:", green, ", yellow:", yellow, ", red(list):", red)

fruits3 = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits3
print("Using * in middle -> green:", green, ", tropic:", tropic, ", red:", red)

# ----------------------------
print("\n--- 5. Looping Through Tuples ---")
loop_tuple = ("apple", "banana", "cherry")
print("For loop:")
for item in loop_tuple:
    print(" -", item)

print("Loop by index:")
for i in range(len(loop_tuple)):
    print(f"Index {i} ->", loop_tuple[i])

print("While loop:")
i = 0
while i < len(loop_tuple):
    print(f"Index {i} ->", loop_tuple[i])
    i += 1

# ----------------------------
print("\n--- 6. Joining & Multiplying Tuples ---")
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print("Joining two tuples:", tuple3)

fruits = ("apple", "banana", "cherry")
repeated = fruits * 2
print("Multiplying tuple by 2:", repeated)

# ----------------------------
print("\n--- 7. Tuple Methods ---")
numbers = (1, 2, 3, 2, 4, 2, 5)
print("Numbers tuple:", numbers)
print("count(2) ->", numbers.count(2))
print("index(4) ->", numbers.index(4))

# ----------------------------
print("\n--- 8. Comparison with LIST methods ---")
# Lists are mutable, unlike tuples
mylist = ["apple", "banana", "cherry"]
print("Original list:", mylist)

mylist.append("orange")
print("After append:", mylist)

mylist.insert(1, "kiwi")
print("After insert at index 1:", mylist)

mylist.remove("banana")
print("After remove 'banana':", mylist)

popped = mylist.pop()
print("After pop (removed last):", mylist, "| popped item:", popped)

mylist.sort()
print("After sort:", mylist)

mylist.reverse()
print("After reverse:", mylist)

copy_list = mylist.copy()
print("Copied list:", copy_list)

print("Final List Methods Demo Done")

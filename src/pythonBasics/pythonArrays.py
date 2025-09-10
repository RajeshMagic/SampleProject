"""
=========================================
Python Arrays (Using Lists)
=========================================

Note:
- Python does not have a built-in array data type.
- We use LISTS as arrays in Python.
- For real numeric arrays, we usually use NumPy library.
"""

print("\n==========================")
print("1. Creating an Array (List)")
print("==========================")

cars = ["Ford", "Volvo", "BMW"]
print("Initial array:", cars)
print("Important Note: In Python, lists act like arrays and can hold multiple values.")


print("\n==========================")
print("2. Accessing & Modifying Elements")
print("==========================")

print("First element (cars[0]):", cars[0])
cars[0] = "Toyota"
print("Modified first element:", cars)


print("\n==========================")
print("3. Length of an Array")
print("==========================")

print("Number of elements in cars:", len(cars))
print("Important Note: len() gives total items. Index starts from 0, so last index = len-1.")


print("\n==========================")
print("4. Looping Through Arrays")
print("==========================")

print("Looping with for-in:")
for car in cars:
    print("Car:", car)


print("\n==========================")
print("5. Adding Elements")
print("==========================")

cars.append("Honda")
print("After append('Honda'):", cars)

cars.insert(1, "Audi")
print("After insert(1, 'Audi'):", cars)

print("Important Note: append() always adds at end, insert(pos, value) adds at specific index.")


print("\n==========================")
print("6. Removing Elements")
print("==========================")

cars.pop(1)  # removes element at index 1
print("After pop(1):", cars)

cars.remove("Volvo")  # removes first occurrence of 'Volvo'
print("After remove('Volvo'):", cars)

print("Important Note: pop(index) removes by position, remove(value) removes by value.")


print("\n==========================")
print("7. Array/List Methods")
print("==========================")

nums = [10, 20, 30, 20, 40]

# copy()
nums_copy = nums.copy()
print("Original nums:", nums)
print("Copied nums:", nums_copy)

# count()
print("Count of 20 in nums:", nums.count(20))

# extend()
extra = [50, 60]
nums.extend(extra)
print("After extend([50,60]):", nums)

# index()
print("Index of value 40:", nums.index(40))

# reverse()
nums.reverse()
print("After reverse():", nums)

# sort()
nums.sort()
print("After sort():", nums)

# clear()
temp = nums.copy()
temp.clear()
print("After clear():", temp)

print("Important Note: These methods make list manipulation powerful and flexible.")


print("\n==========================")
print("8. Summary")
print("==========================")
print("We demonstrated:")
print("- Creating arrays (lists)")
print("- Accessing & modifying elements")
print("- len() function")
print("- Looping through arrays")
print("- Adding/removing elements")
print("- List methods: append, insert, pop, remove, copy, count, extend, index, reverse, sort, clear")
print("\nPython lists are very powerful and used everywhere instead of arrays.")

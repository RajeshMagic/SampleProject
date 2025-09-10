# ==========================================
# PYTHON SETS - DEMONSTRATION
# ==========================================

print("\n========== 1. Creating Sets ==========")

# A set is an unordered collection with no duplicates
myset = {"apple", "banana", "cherry"}
print("Created Set:", myset)

# Duplicate values are ignored
dup_set = {"apple", "banana", "cherry", "apple"}
print("Duplicate values are removed automatically:", dup_set)

# True and 1 are treated as the same value
bool_set = {"apple", True, 1, 2}
print("Note: True and 1 are considered same ->", bool_set)

# False and 0 are also treated as the same value
bool_set2 = {"apple", False, 0, True}
print("Note: False and 0 are considered same ->", bool_set2)

# Length of a set
print("Length of myset:", len(myset))

# Sets can store different data types
mixed_set = {"abc", 34, True, 40, "male"}
print("Mixed data type set:", mixed_set)

# Constructor
constructed = set(("apple", "banana", "cherry"))
print("Set created using set() constructor:", constructed)

# -------------------------------
print("\n========== 2. Accessing Set Items ==========")

# Sets are unordered -> cannot access by index
# But you can loop through or check membership
thisset = {"apple", "banana", "cherry"}
print("Original Set:", thisset)

print("Looping through set:")
for item in thisset:
    print(" -", item)

print("Check if 'banana' in set:", "banana" in thisset)
print("Check if 'kiwi' not in set:", "kiwi" not in thisset)

# -------------------------------
print("\n========== 3. Adding Items to Sets ==========")

thisset = {"apple", "banana", "cherry"}
print("Original:", thisset)

thisset.add("orange")
print("After add('orange'):", thisset)

# Add another set
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print("After update() with another set:", thisset)

# Add list/tuple
mylist = ["kiwi", "grape"]
thisset.update(mylist)
print("After update() with a list:", thisset)

# -------------------------------
print("\n========== 4. Removing Items from Sets ==========")

thisset = {"apple", "banana", "cherry"}
print("Original:", thisset)

thisset.remove("banana")   # raises error if not present
print("After remove('banana'):", thisset)

thisset.discard("apple")   # no error if item not present
print("After discard('apple'):", thisset)

# Pop removes a random item (since unordered)
removed = thisset.pop()
print("Pop() removed:", removed, "| Remaining:", thisset)

thisset.clear()
print("After clear():", thisset)

thisset = {"apple", "banana"}
del thisset
print("Note: Set deleted using del (cannot access anymore)")

# -------------------------------
print("\n========== 5. Looping through Sets ==========")

thisset = {"apple", "banana", "cherry"}
print("Loop using for:")
for fruit in thisset:
    print(" -", fruit)

# -------------------------------
print("\n========== 6. Joining and Set Operations ==========")

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

# Union
print("Union with union():", set1.union(set2))
print("Union with | :", set1 | set2)

# Multiple sets union
set3 = {"John", "Elena"}
print("Union of multiple sets:", set1.union(set2, set3))

# Join set and tuple
z = set1.union((4, 5, 6))
print("Union with tuple:", z)

# Update (in-place union)
set1.update(set2)
print("After update(), set1:", set1)

# Intersection
setA = {"apple", "banana", "cherry"}
setB = {"google", "microsoft", "apple"}
print("Intersection with intersection():", setA.intersection(setB))
print("Intersection with & :", setA & setB)

# intersection_update modifies the set
setA.intersection_update(setB)
print("After intersection_update, setA:", setA)

# Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "apple"}
print("Difference set1 - set2:", set1.difference(set2))
set1.difference_update(set2)
print("After difference_update, set1:", set1)

# Symmetric Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "apple"}
print("Symmetric Difference:", set1.symmetric_difference(set2))
print("Symmetric Difference with ^ :", set1 ^ set2)

set1.symmetric_difference_update(set2)
print("After symmetric_difference_update, set1:", set1)

# -------------------------------
print("\n========== 7. Other Useful Set Methods ==========")

set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "kiwi"}
set3 = {"cherry"}

# Copy
copy_set = set1.copy()
print("Copy of set1:", copy_set)

# isdisjoint -> True if no common elements
print("isdisjoint (set1 vs set2):", set1.isdisjoint(set2))

# issubset
print("issubset (set3 <= set1):", set3.issubset(set1))

# issuperset
print("issuperset (set1 >= set3):", set1.issuperset(set3))

# -------------------------------
print("\n========== IMPORTANT NOTES ==========")
print("1. Sets are unordered -> no indexing or slicing")
print("2. Sets do not allow duplicates (True=1, False=0 are treated same)")
print("3. Items are immutable (cannot change), but sets are mutable (can add/remove items)")
print("4. Useful for mathematical set operations: union, intersection, difference")
print("5. Use frozenset() if you want an immutable set")

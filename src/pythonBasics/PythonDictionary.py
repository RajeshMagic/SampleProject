# ==========================================
# PYTHON DICTIONARIES - DEMONSTRATION
# ==========================================

print("\n========== 1. Creating Dictionaries ==========")

# Basic dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("Dictionary:", thisdict)

# Duplicate keys overwrite
dup_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020   # overwrites 1964
}
print("Duplicate key example:", dup_dict)

# Length of dictionary
print("Length of dictionary:", len(thisdict))

# Dictionary with different data types
car = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print("Dictionary with different types:", car)

# Using dict() constructor
person = dict(name="John", age=36, country="Norway")
print("Dictionary using dict() constructor:", person)

# Type check
print("Type of dictionary:", type(thisdict))

# -------------------------------
print("\n========== 2. Accessing Dictionary Items ==========")

print("Access by key:", thisdict["model"])
print("Access with get():", thisdict.get("model"))

# Keys view
print("Keys view:", thisdict.keys())

# Values view
print("Values view:", thisdict.values())

# Items view
print("Items view:", thisdict.items())

# Keys, values, and items reflect changes
print("Before adding color:", car.keys())
car["color"] = "white"
print("After adding color:", car.keys())

print("Before updating year:", car.values())
car["year"] = 2020
print("After updating year:", car.values())

# Check if key exists
if "model" in thisdict:
    print("Yes, 'model' key exists in dictionary")

# -------------------------------
print("\n========== 3. Changing and Adding Items ==========")

thisdict["year"] = 2018
print("Changed year value:", thisdict)

# Using update() to change existing item
thisdict.update({"year": 2022})
print("After update() year:", thisdict)

# Adding new key
thisdict["color"] = "red"
print("Added color key:", thisdict)

# Using update() to add new key
thisdict.update({"engine": "V8"})
print("After update() with new key:", thisdict)

# -------------------------------
print("\n========== 4. Removing Items ==========")

sample = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "red"
}
print("Original Dictionary:", sample)

# pop() removes specified key
sample.pop("model")
print("After pop('model'):", sample)

# popitem() removes last inserted item
sample.popitem()
print("After popitem():", sample)

# del removes a specific key
del sample["year"]
print("After del sample['year']:", sample)

# clear empties dictionary
sample.clear()
print("After clear():", sample)

# del deletes dictionary completely
sample = {"brand": "Ford"}
del sample
print("Note: Dictionary deleted with del (cannot access anymore)")

# -------------------------------
print("\n========== 5. Looping Through Dictionary ==========")

loop_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("Loop through keys:")
for key in loop_dict:
    print(" -", key)

print("Loop through values using keys:")
for key in loop_dict:
    print(" -", loop_dict[key])

print("Loop through values() method:")
for val in loop_dict.values():
    print(" -", val)

print("Loop through keys() method:")
for key in loop_dict.keys():
    print(" -", key)

print("Loop through items() (key-value pairs):")
for k, v in loop_dict.items():
    print(f" - {k}: {v}")

# -------------------------------
print("\n========== 6. Copying Dictionaries ==========")

copy1 = loop_dict.copy()
print("Copy using copy():", copy1)

copy2 = dict(loop_dict)
print("Copy using dict():", copy2)

# -------------------------------
print("\n========== 7. Nested Dictionaries ==========")

# Nested dictionary
myfamily = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011}
}
print("Nested Dictionary:", myfamily)

# Access nested dictionary item
print("Child2 name:", myfamily["child2"]["name"])

# Loop through nested dictionary
print("Looping through nested dictionary:")
for child, details in myfamily.items():
    print(child)
    for k, v in details.items():
        print("  -", k, ":", v)

# -------------------------------
print("\n========== 8. Dictionary Methods ==========")

d = {"a": 1, "b": 2, "c": 3}

# clear()
d_copy = d.copy()
d_copy.clear()
print("clear() ->", d_copy)

# fromkeys()
keys = ("x", "y", "z")
new_dict = dict.fromkeys(keys, 0)
print("fromkeys() ->", new_dict)

# get()
print("get('a') ->", d.get("a"))
print("get('z', 'Not Found') ->", d.get("z", "Not Found"))

# items()
print("items() ->", d.items())

# keys()
print("keys() ->", d.keys())

# pop()
d_copy = d.copy()
d_copy.pop("a")
print("pop('a') ->", d_copy)

# popitem()
d_copy = d.copy()
d_copy.popitem()
print("popitem() ->", d_copy)

# setdefault()
d_copy = d.copy()
print("setdefault('a') ->", d_copy.setdefault("a", 100))
print("setdefault('z', 100) ->", d_copy.setdefault("z", 100))
print("After setdefault() ->", d_copy)

# update()
d_copy.update({"d": 4})
print("After update({'d':4}) ->", d_copy)

# values()
print("values() ->", d_copy.values())

# -------------------------------
print("\n========== IMPORTANT NOTES ==========")
print("1. Dictionaries store data in key:value pairs")
print("2. Keys must be unique (duplicate keys overwrite)")
print("3. Values can be any data type (even lists, sets, or other dicts)")
print("4. Dictionaries are mutable -> can change, add, remove items")
print("5. Since Python 3.7, dictionaries are ordered")
print("6. Use copy() or dict() to copy safely (not just assignment)")
print("7. Nested dictionaries allow structured data representation")
print("8. Methods like get(), setdefault(), update() are very useful in practice")

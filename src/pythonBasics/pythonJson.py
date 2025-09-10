# ===============================================================
# PYTHON JSON - DEMONSTRATION
# ===============================================================
# JSON = JavaScript Object Notation
# - Lightweight data format used for storing and exchanging data.
# - Python has a built-in 'json' module to handle JSON.
#
# In Python:
#   - json.loads()  -> Converts JSON string into Python object
#   - json.dumps()  -> Converts Python object into JSON string
#
# This demo will show:
#   1. Parsing JSON (string -> Python object)
#   2. Converting Python objects to JSON strings
#   3. Supported data types mapping
#   4. Formatting JSON with indent & separators
#   5. Sorting JSON keys
# ===============================================================

import json

print("\n==============================")
print(" 1. PARSING JSON (string -> Python object) ")
print("==============================")

# Example JSON string
json_str = '{ "name":"John", "age":30, "city":"New York"}'
print("Original JSON string:", json_str)

# Convert JSON string to Python dict
parsed = json.loads(json_str)
print("After json.loads():", parsed)
print("Accessing a value (age):", parsed["age"])
print("Important Note: json.loads() converts JSON text into a Python dictionary.\n")


print("==============================")
print(" 2. PYTHON OBJECT -> JSON STRING ")
print("==============================")

# Python dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert dict to JSON string
json_str2 = json.dumps(person)
print("Original Python dict:", person)
print("Converted JSON string:", json_str2)
print("Important Note: json.dumps() converts Python object to JSON string.\n")


print("==============================")
print(" 3. JSON SUPPORTS MULTIPLE PYTHON DATA TYPES ")
print("==============================")

print("dict ->", json.dumps({"name": "John", "age": 30}))
print("list ->", json.dumps(["apple", "banana"]))
print("tuple ->", json.dumps(("apple", "banana")))
print("string ->", json.dumps("hello"))
print("int ->", json.dumps(42))
print("float ->", json.dumps(31.76))
print("True ->", json.dumps(True))
print("False ->", json.dumps(False))
print("None ->", json.dumps(None))

print("\nImportant Note: Python types are mapped to JSON equivalents:")
print("Python dict -> JSON Object")
print("Python list/tuple -> JSON Array")
print("Python str -> JSON String")
print("Python int/float -> JSON Number")
print("Python True/False -> JSON true/false")
print("Python None -> JSON null\n")


print("==============================")
print(" 4. COMPLEX PYTHON OBJECT -> JSON ")
print("==============================")

complex_obj = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

json_complex = json.dumps(complex_obj)
print("Python object:", complex_obj)
print("JSON string:", json_complex)
print("Important Note: Nested structures (lists, dicts inside dicts) are handled correctly.\n")


print("==============================")
print(" 5. FORMATTING JSON OUTPUT ")
print("==============================")

# Pretty print with indentation
pretty_json = json.dumps(complex_obj, indent=4)
print("Pretty formatted JSON:\n", pretty_json)

# Custom separators
custom_sep = json.dumps(complex_obj, indent=4, separators=(". ", " = "))
print("\nCustom separators JSON:\n", custom_sep)

print("Important Note: Use indent for readability, separators to change default formatting.\n")


print("==============================")
print(" 6. SORTING JSON KEYS ")
print("==============================")

sorted_json = json.dumps(complex_obj, indent=4, sort_keys=True)
print("Sorted JSON:\n", sorted_json)
print("Important Note: sort_keys=True arranges dictionary keys alphabetically.\n")


print("==============================")
print(" END OF JSON DEMO ")
print("==============================\n")

# -------------------------------------------
# Python Built-in Data Types - Full Demonstration
# -------------------------------------------

print("========== PYTHON BUILT-IN DATA TYPES DEMO ==========\n")

# Helper function to display value and type
def show(var_name, value):
    print(f"{var_name} = {value} -> type: {type(value)}")

# 1. Text Type
print("1. TEXT TYPE (str):")
x = "Hello World"
show("x", x)
print()

# 2. Numeric Types
print("2. NUMERIC TYPES (int, float, complex):")
x = 20
show("x", x)
x = 20.5
show("x", x)
x = 1j
show("x", x)
print()

# 3. Sequence Types
print("3. SEQUENCE TYPES (list, tuple, range):")
x = ["apple", "banana", "cherry"]
show("x", x)
x = ("apple", "banana", "cherry")
show("x", x)
x = range(6)
show("x", x)
print("Converting range to list for readability:", list(x))
print()

# 4. Mapping Type
print("4. MAPPING TYPE (dict):")
x = {"name": "John", "age": 36}
show("x", x)
print()

# 5. Set Types
print("5. SET TYPES (set, frozenset):")
x = {"apple", "banana", "cherry"}
show("x", x)
x = frozenset({"apple", "banana", "cherry"})
show("x", x)
print()

# 6. Boolean Type
print("6. BOOLEAN TYPE (bool):")
x = True
show("x", x)
print()

# 7. Binary Types
print("7. BINARY TYPES (bytes, bytearray, memoryview):")
x = b"Hello"
show("x", x)
x = bytearray(5)   # creates mutable byte array of length 5
show("x", x)
x = memoryview(bytes(5))  # memory view of byte sequence
show("x", x)
print()

# 8. None Type
print("8. NONE TYPE (NoneType):")
x = None
show("x", x)
print()

print("----------------------------------------------------")
print("   ✅ DEMONSTRATING DATA TYPES USING CONSTRUCTORS")
print("----------------------------------------------------\n")

# TEXT
x = str("Hello World")
show("x", x)

# NUMERIC
x = int(20)
show("x", x)
x = float(20.5)
show("x", x)
x = complex(1j)
show("x", x)

# SEQUENCE
x = list(("apple", "banana", "cherry"))
show("x", x)
x = tuple(("apple", "banana", "cherry"))
show("x", x)
x = range(6)
show("x", x)

# MAPPING
x = dict(name="John", age=36)
show("x", x)

# SETS
x = set(("apple", "banana", "cherry"))
show("x", x)
x = frozenset(("apple", "banana", "cherry"))
show("x", x)

# BOOLEAN
x = bool(5)   # nonzero → True
show("x", x)

# BINARY
x = bytes(5)  # creates 5 null bytes
show("x", x)
x = bytearray(5)
show("x", x)
x = memoryview(bytes(5))
show("x", x)

print("\n========== END OF DATA TYPES DEMO ==========")

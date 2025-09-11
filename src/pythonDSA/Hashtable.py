# ================================================================
# HASH TABLES IN PYTHON - DEMONSTRATION PROGRAM
# ================================================================

print("\n============================")
print(" HASH TABLES IN PYTHON ")
print("============================\n")

print("🔹 A Hash Table is a data structure that stores elements in 'buckets'.")
print("🔹 Each element is placed in a bucket using a hash function.")
print("🔹 Hash Tables allow very FAST insert, search, and delete (O(1) average).")
print("🔹 Compared to Arrays (O(n) search) or Linked Lists (O(n) search),")
print("   Hash Tables are much more efficient for large datasets.\n")

# ================================================================
# Step 1: Create an empty hash table (array of buckets)
# ================================================================
my_list = [None] * 10  # Fixed size hash table with 10 slots
print("Step 1: Created an empty Hash Table with 10 buckets:")
print(my_list, "\n")

# ================================================================
# Step 2: Create a Hash Function
# ================================================================
def hash_function(value):
    """
    Convert a string into a bucket index (0-9).
    Method: Sum Unicode values of characters, take modulo 10.
    """
    sum_of_chars = sum(ord(char) for char in value)
    return sum_of_chars % 10

print("Step 2: Hash Function Example:")
print("'Bob' has hash code:", hash_function('Bob'))
print("Explanation: B=66, o=111, b=98 → Sum=275 → 275 % 10 = 5\n")

# ================================================================
# Step 3: Insert Elements using Hash Function
# ================================================================
def add(name):
    """
    Insert element into hash table using hash function.
    """
    index = hash_function(name)
    my_list[index] = name  # Overwrites if collision occurs
    print(f"Inserted '{name}' at index {index}")

print("Step 3: Inserting elements into Hash Table")
add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
print("Hash Table after insertions:")
print(my_list, "\n")

print("--- Important Note ---")
print("❌ Collisions will overwrite existing values (problem!).")
print("✅ Next, we handle collisions properly using chaining.\n")

# ================================================================
# Step 4: Lookup Elements
# ================================================================
def contains(name):
    """
    Check if element exists in hash table.
    """
    index = hash_function(name)
    return my_list[index] == name

print("Step 4: Looking up elements")
print("'Pete' is in the Hash Table:", contains('Pete'))
print("'Stuart' is in the Hash Table:", contains('Stuart'), "\n")

print("--- Important Note ---")
print("✅ Lookup uses the hash function to go directly to bucket index.")
print("✅ O(1) average time complexity (very fast).")
print("❌ But still fails if collisions overwrite values.\n")

# ================================================================
# Step 5: Handle Collisions using Chaining
# ================================================================
# Rebuild hash table with chaining (each bucket is a list)
my_list = [[] for _ in range(10)]

def add_with_chaining(name):
    """
    Insert element into hash table using chaining to handle collisions.
    """
    index = hash_function(name)
    my_list[index].append(name)
    print(f"Inserted '{name}' into bucket {index}")

def contains_with_chaining(name):
    """
    Check if element exists (with chaining).
    """
    index = hash_function(name)
    return name in my_list[index]

print("Step 5: Handling Collisions with Chaining\n")
add_with_chaining('Bob')
add_with_chaining('Pete')
add_with_chaining('Jones')
add_with_chaining('Lisa')
add_with_chaining('Siri')
add_with_chaining('Stuart')  # Will collide with Lisa at index 3
print("\nHash Table with chaining (buckets can hold multiple values):")
print(my_list, "\n")

print("Lookup with chaining:")
print("'Stuart' is in Hash Table:", contains_with_chaining('Stuart'))
print("'Lisa' is in Hash Table:", contains_with_chaining('Lisa'))
print("'Alex' is in Hash Table:", contains_with_chaining('Alex'), "\n")

print("--- Important Note ---")
print("✅ Collisions are solved by chaining (multiple items per bucket).")
print("✅ Still much faster than searching arrays/linked lists.")
print("❌ Lookup is O(k) in worst-case (k = number of items in same bucket).")
print("✅ But on average, still O(1).\n")

# ================================================================
# USE CASES
# ================================================================
print("📌 USES of Hash Tables:")
print("""
1. Fast lookups (checking membership, e.g. 'is Bob in the set?').
2. Storing unique elements (like phone numbers, usernames).
3. Key-Value pairs (like dictionaries in Python).
4. Databases, caching, compilers, and many algorithms rely on them.
""")

# ================================================================
# END OF DEMO
# ================================================================
print("\n🎯 Demo Complete: Hash Tables in Python (Insert, Lookup, Collisions)\n")

"""
NumPy Random Numbers Tutorial
-----------------------------
This script demonstrates:
1. Concept of random vs pseudo-random.
2. Generating random integers and floats.
3. Creating random arrays (1D, 2D).
4. Generating random numbers from a given array using choice().
"""

from numpy import random

print("\n========== 1. RANDOM vs PSEUDO RANDOM ==========\n")
print("Random ≠ different every time.")
print("Computers use algorithms -> so numbers are pseudo-random (predictable if you know the seed).")
print("True randomness needs external sources (keyboard timings, mouse movement, etc.).")
print("NumPy provides pseudo-random numbers (good enough for simulations, ML, etc.).\n")

print("\n========== 2. GENERATE RANDOM INTEGER ==========\n")

x = random.randint(100)  # random int from 0–100 (exclusive)
print("Random Integer between 0 and 100:", x)
print("Important Note: randint(100) → generates a single integer in range [0, 100).\n")


print("\n========== 3. GENERATE RANDOM FLOAT ==========\n")

x = random.rand()  # random float between 0–1
print("Random Float between 0 and 1:", x)
print("Important Note: rand() → always generates float in [0.0, 1.0).\n")


print("\n========== 4. GENERATE RANDOM ARRAY OF INTEGERS ==========\n")

x = random.randint(100, size=(5))  # 1D array of 5 integers
print("1D Array of 5 Random Integers [0–100):", x)

x = random.randint(100, size=(3, 5))  # 2D array (3 rows, 5 columns)
print("\n2D Array of Random Integers (3x5):\n", x)

print("Important Note: size=(m,n) → creates m rows, n columns.\n")


print("\n========== 5. GENERATE RANDOM ARRAY OF FLOATS ==========\n")

x = random.rand(5)  # 1D array of 5 floats
print("1D Array of 5 Random Floats (0–1):", x)

x = random.rand(3, 5)  # 2D array (3x5) of floats
print("\n2D Array of Random Floats (3x5):\n", x)

print("Important Note: rand(shape) → fills array with floats in [0.0, 1.0).\n")


print("\n========== 6. RANDOM VALUE FROM A CUSTOM ARRAY ==========\n")

x = random.choice([3, 5, 7, 9])  # randomly picks ONE from given array
print("Random Value chosen from [3,5,7,9]:", x)

x = random.choice([3, 5, 7, 9], size=(3, 5))  # 2D random selection
print("\n2D Array Randomly Chosen from [3,5,7,9]:\n", x)

print("Important Note: choice() → picks elements from your list/array randomly.\n")


print("\n========== END OF NUMPY RANDOM DEMO ==========\n")

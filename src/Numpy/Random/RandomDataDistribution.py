"""
NumPy Random Data Distribution Tutorial
---------------------------------------
This script demonstrates:
1. What is data distribution?
2. Random distribution using NumPy.
3. Using choice() with probability values.
4. Generating 1D and 2D random arrays with specified probabilities.
"""

from numpy import random

print("\n========== 1. WHAT IS DATA DISTRIBUTION? ==========\n")
print("Data Distribution = List of all possible values + how often each occurs.")
print("In statistics, this describes probabilities of values.")
print("Example: In a dice roll, numbers 1-6 each have equal probability = 1/6.\n")

print("NumPy provides random distributions using the random module.\n")
print("We can generate values with specific probabilities using choice(p=...).\n")


print("\n========== 2. RANDOM DISTRIBUTION USING CHOICE() ==========\n")

# Generate a 1D array with weighted probabilities
x = random.choice([3, 5, 7, 9], 
                  p=[0.1, 0.3, 0.6, 0.0], 
                  size=(100))

print("Generated 1D Array of 100 values:\n", x)
print("\nImportant Note:")
print(" - p=[0.1, 0.3, 0.6, 0.0] means:")
print("   10% chance for 3, 30% chance for 5, 60% chance for 7, and 0% chance for 9.")
print(" - Sum of probabilities MUST = 1.")
print(" - Value '9' will NEVER occur because probability = 0.\n")


print("\n========== 3. GENERATING 2D DISTRIBUTIONS ==========\n")

# Generate a 2D array with probabilities
x = random.choice([3, 5, 7, 9], 
                  p=[0.1, 0.3, 0.6, 0.0], 
                  size=(3, 5))

print("Generated 2D Array of shape (3x5):\n", x)

print("\nImportant Notes:")
print(" - Size=(3,5) → 3 rows and 5 columns.")
print(" - Distribution rule still applies per element.")
print(" - Each value generated independently with defined probabilities.\n")


print("\n========== 4. OBSERVATION ==========\n")
print("Even if you run this code 1000 times, '9' will NEVER appear (p=0).")
print("Most values will be '7' (since p=0.6 → 60% chance).")
print("Values '3' and '5' appear less often (10% and 30% chance respectively).\n")

print("\n========== END OF RANDOM DATA DISTRIBUTION DEMO ==========\n")

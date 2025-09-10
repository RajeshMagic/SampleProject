# ==============================================================
# LINEAR SEARCH DEMONSTRATION IN PYTHON
# ==============================================================
# This program demonstrates:
#   1. Using "in" operator for quick existence check
#   2. Implementing Linear Search function
#   3. Finding index of target value
#   4. Explaining time complexity (O(n))
#   5. Example outputs for better understanding
# ==============================================================

# ---------------------------------------------------------------
# 1. QUICK CHECK USING "in" OPERATOR
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 1: CHECK IF VALUE EXISTS USING 'in' OPERATOR ")
print("==============================")

mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]
target = 4

print(f"List to search in: {mylist}")
print(f"Target value: {target}")

# Quick check
if target in mylist:
    print(f"✅ Found! The value {target} exists in the list.")
else:
    print(f"❌ Not Found! The value {target} is not in the list.")

print("Important Note: Using 'in' operator only tells if the value exists,")
print("but does not give the index where the value is located.\n")


# ---------------------------------------------------------------
# 2. LINEAR SEARCH FUNCTION IMPLEMENTATION
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 2: IMPLEMENT LINEAR SEARCH FUNCTION ")
print("==============================")

def linearSearch(arr, targetVal):
    """
    Perform Linear Search on array.
    Args:
        arr: list of elements
        targetVal: value to search for
    Returns:
        Index of element if found, else -1
    """
    for i in range(len(arr)):
        print(f"Checking index {i}: value = {arr[i]}")  # Show search process
        if arr[i] == targetVal:
            return i  # Found target
    return -1  # Not found


# ---------------------------------------------------------------
# 3. FIND INDEX USING LINEAR SEARCH
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 3: FIND INDEX USING LINEAR SEARCH ")
print("==============================")

result = linearSearch(mylist, target)

if result != -1:
    print(f"✅ Target {target} found at index {result}")
else:
    print(f"❌ Target {target} not found in list")


# ---------------------------------------------------------------
# 4. TRY SEARCHING FOR A NON-EXISTENT VALUE
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 4: TRY SEARCHING FOR NON-EXISTENT VALUE ")
print("==============================")

missing_target = 99
result = linearSearch(mylist, missing_target)

if result != -1:
    print(f"✅ Target {missing_target} found at index {result}")
else:
    print(f"❌ Target {missing_target} not found in list (returned -1)")


# ---------------------------------------------------------------
# 5. TIME COMPLEXITY EXPLANATION
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 5: TIME COMPLEXITY EXPLANATION ")
print("==============================")

print("🔹 If the target is the FIRST element -> Best Case = O(1)")
print("🔹 If the target is the LAST element or NOT PRESENT -> Worst Case = O(n)")
print("🔹 On average, Linear Search takes O(n/2) ~ O(n) comparisons.")
print("\nExample:")
print("Searching for 3 (first element) → 1 comparison")
print("Searching for 6 (last element) → 9 comparisons")
print("Searching for 99 (not present) → 9 comparisons (full list checked)")

print("\n==============================")
print(" END OF LINEAR SEARCH DEMO ")
print("==============================")

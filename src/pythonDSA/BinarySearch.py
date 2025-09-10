# ==============================================================
# BINARY SEARCH DEMONSTRATION IN PYTHON
# ==============================================================
# This program demonstrates:
#   1. Manual step-by-step explanation of Binary Search
#   2. Implementation of Binary Search function
#   3. Example when value is FOUND
#   4. Example when value is NOT FOUND
#   5. Time Complexity explanation (O(log n))
# ==============================================================

# ---------------------------------------------------------------
# 1. MANUAL WALKTHROUGH (conceptual)
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 1: MANUAL WALKTHROUGH ")
print("==============================")

arr_manual = [2, 3, 7, 7, 11, 15, 25]
target_manual = 11

print(f"Array: {arr_manual}")
print(f"Target value: {target_manual}")

print("\nManual Search Steps:")
print("Step 1: Middle of array → index 3 → value = 7")
print("Step 2: 7 < 11 → Search in RIGHT half [11, 15, 25]")
print("Step 3: New middle = index 5 → value = 15")
print("Step 4: 15 > 11 → Search LEFT half → index 4 → value = 11")
print("Step 5: ✅ Found target 11 at index 4")
print("Important Note: Binary Search only works on a **sorted array**\n")


# ---------------------------------------------------------------
# 2. BINARY SEARCH FUNCTION IMPLEMENTATION
# ---------------------------------------------------------------
def binarySearch(arr, targetVal):
    """
    Perform Binary Search on a sorted array.
    Args:
        arr: list of sorted elements
        targetVal: value to search for
    Returns:
        Index of element if found, else -1
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        print(f"Checking middle index {mid}: value = {arr[mid]}")  # Trace

        if arr[mid] == targetVal:
            return mid  # Found target

        if arr[mid] < targetVal:
            print(f"Target {targetVal} is greater → Move RIGHT")
            left = mid + 1
        else:
            print(f"Target {targetVal} is smaller → Move LEFT")
            right = mid - 1

    return -1  # Not found


# ---------------------------------------------------------------
# 3. EXAMPLE: VALUE FOUND
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 2: BINARY SEARCH (VALUE FOUND) ")
print("==============================")

mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11

print(f"Sorted list: {mylist}")
print(f"Target to search: {target}\n")

result = binarySearch(mylist, target)

if result != -1:
    print(f"✅ Target {target} found at index {result}")
else:
    print(f"❌ Target {target} not found")


# ---------------------------------------------------------------
# 4. EXAMPLE: VALUE NOT FOUND
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 3: BINARY SEARCH (VALUE NOT FOUND) ")
print("==============================")

target = 20
print(f"Target to search: {target}\n")

result = binarySearch(mylist, target)

if result != -1:
    print(f"✅ Target {target} found at index {result}")
else:
    print(f"❌ Target {target} not found (returned -1)")


# ---------------------------------------------------------------
# 5. TIME COMPLEXITY EXPLANATION
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 4: TIME COMPLEXITY EXPLANATION ")
print("==============================")

print("🔹 Each step halves the search space.")
print("🔹 Best Case: Target is at the middle → O(1)")
print("🔹 Worst Case: Target not present → O(log₂ n) steps")
print("🔹 Average Case: Still O(log₂ n)")
print("\nExample with n = 1024 elements:")
print("Linear Search → up to 1024 checks")
print("Binary Search → log₂(1024) = 10 checks only")

print("\n==============================")
print(" END OF BINARY SEARCH DEMO ")
print("==============================")

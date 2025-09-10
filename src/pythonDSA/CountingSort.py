# ==============================================================
# COUNTING SORT DEMONSTRATION IN PYTHON
# ==============================================================
# This program demonstrates:
#   1. Manual walkthrough of Counting Sort
#   2. Implementation of countingSort() method
#   3. Step-by-step console outputs
#   4. Explanation of algorithm conditions & limitations
#   5. Time Complexity discussion
# ==============================================================


# ---------------------------------------------------------------
# 1. MANUAL WALKTHROUGH
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 1: MANUAL WALKTHROUGH ")
print("==============================")

arr_manual = [2, 3, 0, 2, 3, 2]
print(f"Unsorted Array: {arr_manual}")

print("\nManual Steps:")
print("Step 1: Create counting array of size (max+1) = 4 → [0, 0, 0, 0]")
print("Step 2: Count occurrences:")
print("   Encounter 2 → [0, 0, 1, 0]")
print("   Encounter 3 → [0, 0, 1, 1]")
print("   Encounter 0 → [1, 0, 1, 1]")
print("   Encounter 2 → [1, 0, 2, 1]")
print("   Encounter 3 → [1, 0, 2, 2]")
print("   Encounter 2 → [1, 0, 3, 2]")

print("\nStep 3: Rebuild sorted array from counting array:")
print("   Value 0 → Add 1 time → [0]")
print("   Value 1 → Add 0 times → [0]")
print("   Value 2 → Add 3 times → [0, 2, 2, 2]")
print("   Value 3 → Add 2 times → [0, 2, 2, 2, 3, 3]")

print("\n✅ Final Sorted Array: [0, 2, 2, 2, 3, 3]")

print("\nImportant Notes:")
print("➡ Counting Sort does NOT compare elements, unlike Bubble/Quick/Insertion Sort.")
print("➡ Works ONLY for non-negative integers.")
print("➡ Efficient when range of values (k) is much smaller than number of elements (n).")
print("➡ Inefficient if k is very large compared to n.\n")


# ---------------------------------------------------------------
# 2. COUNTING SORT IMPLEMENTATION
# ---------------------------------------------------------------
def countingSort(arr):
    """
    Counting Sort implementation.
    Args:
        arr (list): List of non-negative integers
    Returns:
        list: Sorted list
    """

    if len(arr) == 0:
        return arr

    max_val = max(arr)   # Find maximum value in array
    count = [0] * (max_val + 1)  # Create counting array

    print("\n==============================")
    print(" STEP 2: COUNTING SORT EXECUTION ")
    print("==============================")
    print(f"Original Array: {arr}")
    print(f"Created counting array of size {max_val+1}: {count}")

    # Count occurrences
    for num in arr:
        count[num] += 1
        print(f"Counting value {num} → {count}")

    # Build sorted array
    sorted_arr = []
    for i in range(len(count)):
        while count[i] > 0:
            sorted_arr.append(i)
            count[i] -= 1
            print(f"Placing value {i} → {sorted_arr} (count now: {count})")

    return sorted_arr


# ---------------------------------------------------------------
# 3. DEMONSTRATION WITH SAMPLE LIST
# ---------------------------------------------------------------
mylist = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
print("\n==============================")
print(" STEP 3: RUN COUNTING SORT ")
print("==============================")
print(f"Unsorted List: {mylist}")

mysortedlist = countingSort(mylist)
print(f"\n✅ Final Sorted List: {mysortedlist}\n")

print("Important Notes:")
print("➡ Counting Sort modifies data by rebuilding array, not by swapping elements.")
print("➡ Useful when data range is small and values are repeated often.\n")


# ---------------------------------------------------------------
# 4. TIME COMPLEXITY
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 4: TIME COMPLEXITY ")
print("==============================")

print("🔹 Time Complexity: O(n + k)")
print("   - n = number of elements")
print("   - k = range of values (max value in array + 1)")

print("\nScenarios:")
print("➡ Best Case: O(n) (when k << n)")
print("➡ Average Case: O(n + k)")
print("➡ Worst Case: O(n + k), but inefficient if k >> n")

print("\nExample:")
print("   If n = 10, k = 6 → O(16) ≈ O(n)")
print("   If n = 10, k = 10,000 → O(10,010) ≈ ineffective!")

print("\n✅ Counting Sort is powerful but has limitations.")
print("   Not suitable for floating-point numbers, strings, or negative values.\n")

print("==============================")
print(" END OF COUNTING SORT DEMO ")
print("==============================")

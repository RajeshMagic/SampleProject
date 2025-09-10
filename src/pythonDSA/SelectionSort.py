# ==============================================================
# SELECTION SORT DEMONSTRATION IN PYTHON
# ==============================================================
# This program demonstrates:
#   1. Manual walkthrough of Selection Sort
#   2. Basic Selection Sort implementation (with shifting problem)
#   3. Improved Selection Sort implementation (using swap)
#   4. Time Complexity explanation
# ==============================================================


# ---------------------------------------------------------------
# 1. MANUAL WALKTHROUGH
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 1: MANUAL WALKTHROUGH ")
print("==============================")

arr_manual = [7, 12, 9, 11, 3]
print(f"Unsorted Array: {arr_manual}")

print("\nManual Steps:")
print("Step 1: Find lowest value → 3")
print("Move 3 to front → [3, 7, 12, 9, 11]")

print("Step 2: Next lowest (from remaining) → 7 (already in place)")
print("[3, 7, 12, 9, 11]")

print("Step 3: Next lowest → 9")
print("Swap with 12 → [3, 7, 9, 12, 11]")

print("Step 4: Next lowest → 11")
print("Swap with 12 → [3, 7, 9, 11, 12]")

print("\n✅ Final Sorted Array: [3, 7, 9, 11, 12]")

print("\nImportant Note:")
print("➡ Selection Sort repeatedly selects the MINIMUM value and moves it forward.\n")


# ---------------------------------------------------------------
# 2. BASIC SELECTION SORT (with shifting problem)
# ---------------------------------------------------------------
def selection_sort_shift(arr):
    """
    Selection Sort (using pop + insert).
    This works but causes unnecessary shifting of elements.
    """
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Remove minimum and insert it at correct position
        min_value = arr.pop(min_index)
        arr.insert(i, min_value)
        print(f"After pass {i+1}: {arr}")
    return arr


print("\n==============================")
print(" STEP 2: BASIC SELECTION SORT ")
print("==============================")

mylist = [64, 34, 25, 5, 22, 11, 90, 12]
print(f"Original List: {mylist}\n")

sorted_list = selection_sort_shift(mylist.copy())
print(f"\n✅ Final Sorted List: {sorted_list}\n")

print("⚠️ Important Note:")
print("This version uses POP + INSERT which causes shifting of elements.")
print("That makes it less efficient internally.\n")


# ---------------------------------------------------------------
# 3. IMPROVED SELECTION SORT (using swap)
# ---------------------------------------------------------------
def selection_sort_swap(arr):
    """
    Improved Selection Sort (using swapping instead of shifting).
    This avoids costly shifting operations.
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap values instead of shifting
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"After pass {i+1}: {arr}")
    return arr


print("\n==============================")
print(" STEP 3: IMPROVED SELECTION SORT ")
print("==============================")

mylist2 = [64, 34, 25, 12, 22, 11, 90, 5]
print(f"Original List: {mylist2}\n")

sorted_list2 = selection_sort_swap(mylist2.copy())
print(f"\n✅ Final Sorted List: {sorted_list2}\n")

print("✅ Important Note:")
print("Swapping is better than shifting → Faster & more efficient.\n")


# ---------------------------------------------------------------
# 4. TIME COMPLEXITY
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 4: TIME COMPLEXITY ")
print("==============================")

print("🔹 Selection Sort always compares every element with others.")
print("🔹 Best Case: O(n²) → Even if array is sorted, it must check all.")
print("🔹 Worst Case: O(n²) → When array is reversed.")
print("\nExample:")
print("n = 10 → ~100 comparisons")
print("n = 100 → ~10,000 comparisons")
print("➡ Similar to Bubble Sort, not efficient for large arrays.")

print("\n==============================")
print(" END OF SELECTION SORT DEMO ")
print("==============================")

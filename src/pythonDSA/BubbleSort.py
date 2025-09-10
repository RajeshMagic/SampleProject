# ==============================================================
# BUBBLE SORT DEMONSTRATION IN PYTHON
# ==============================================================
# This program demonstrates:
#   1. Manual run-through example of Bubble Sort
#   2. Normal Bubble Sort implementation
#   3. Improved Bubble Sort implementation (optimized)
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

print("\nManual Steps (first pass only):")
print("Compare 7 and 12 → No Swap")
print("[7, 12, 9, 11, 3]")

print("Compare 12 and 9 → Swap")
print("[7, 9, 12, 11, 3]")

print("Compare 12 and 11 → Swap")
print("[7, 9, 11, 12, 3]")

print("Compare 12 and 3 → Swap")
print("[7, 9, 11, 3, 12]")

print("\nImportant Note:")
print("➡ Each pass bubbles the largest element to the end.\n")


# ---------------------------------------------------------------
# 2. STANDARD BUBBLE SORT
# ---------------------------------------------------------------
def bubble_sort(arr):
    """
    Standard Bubble Sort algorithm.
    Sorts the array in ascending order.
    """
    n = len(arr)
    for i in range(n - 1):  # Outer loop (n-1 passes)
        for j in range(n - i - 1):  # Inner loop
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
        # Show intermediate result
        print(f"After pass {i + 1}: {arr}")
    return arr


print("\n==============================")
print(" STEP 2: STANDARD BUBBLE SORT ")
print("==============================")

mylist = [64, 34, 25, 12, 22, 11, 90, 5]
print(f"Original list: {mylist}\n")

sorted_list = bubble_sort(mylist.copy())
print(f"\n✅ Final Sorted List: {sorted_list}\n")


# ---------------------------------------------------------------
# 3. IMPROVED BUBBLE SORT (OPTIMIZED)
# ---------------------------------------------------------------
def bubble_sort_optimized(arr):
    """
    Improved Bubble Sort algorithm.
    Stops early if no swaps are made in a pass.
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        print(f"After pass {i + 1}: {arr}")
        if not swapped:  # If no swaps, array is already sorted
            print("➡ No swaps done. Array is already sorted. Stopping early.")
            break
    return arr


print("\n==============================")
print(" STEP 3: IMPROVED BUBBLE SORT ")
print("==============================")

mylist2 = [7, 3, 9, 12, 11]
print(f"Original list: {mylist2}\n")

sorted_list2 = bubble_sort_optimized(mylist2.copy())
print(f"\n✅ Final Sorted List: {sorted_list2}\n")


# ---------------------------------------------------------------
# 4. TIME COMPLEXITY EXPLANATION
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 4: TIME COMPLEXITY ")
print("==============================")

print("🔹 Bubble Sort compares adjacent values and swaps if needed.")
print("🔹 For an array of n elements, it does n passes → O(n²).")
print("🔹 Best Case (Optimized Version): O(n) when array is already sorted.")
print("🔹 Worst Case: O(n²) when array is reversed.")
print("\nExample:")
print("n = 10 → up to 100 comparisons")
print("n = 100 → up to 10,000 comparisons")

print("\n==============================")
print(" END OF BUBBLE SORT DEMO ")
print("==============================")

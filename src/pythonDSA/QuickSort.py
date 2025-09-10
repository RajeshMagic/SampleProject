# ==============================================================
# QUICKSORT DEMONSTRATION IN PYTHON
# ==============================================================
# This program demonstrates:
#   1. Manual walkthrough of Quicksort
#   2. Implementation of partition() method
#   3. Implementation of recursive quicksort()
#   4. Console outputs after each partition
#   5. Time Complexity explanation
# ==============================================================


# ---------------------------------------------------------------
# 1. MANUAL WALKTHROUGH
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 1: MANUAL WALKTHROUGH ")
print("==============================")

arr_manual = [11, 9, 12, 7, 3]
print(f"Unsorted Array: {arr_manual}")

print("\nManual Steps:")
print("Step 1: Choose pivot = 3 (last element)")
print("        Swap 3 with 11 → [3, 9, 12, 7, 11]")
print("Step 2: 3 is now in correct place. Left side = [], Right side = [9,12,7,11]")

print("Step 3: New pivot = 11 (last element of right side)")
print("        Move 7 left of 11, keep 12 right → [3, 9, 7, 12, 11]")
print("        Swap pivot 11 with 12 → [3, 9, 7, 11, 12]")

print("Step 4: Pivot 11 in place. Now sort [9, 7].")
print("Step 5: Pivot = 7 → swap with 9 → [3, 7, 9, 11, 12]")

print("\n✅ Final Sorted Array: [3, 7, 9, 11, 12]")

print("\nImportant Note:")
print("➡ Quicksort repeatedly partitions the array around a pivot.")
print("➡ Elements smaller than pivot go left, larger go right.\n")


# ---------------------------------------------------------------
# 2. PARTITION METHOD
# ---------------------------------------------------------------
def partition(array, low, high):
    """
    Partition method:
    Chooses pivot, places smaller elements on left,
    larger elements on right, and returns pivot index.
    """
    pivot = array[high]  # Choosing last element as pivot
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    # Swap pivot into correct position
    array[i+1], array[high] = array[high], array[i+1]
    return i+1


# ---------------------------------------------------------------
# 3. QUICKSORT METHOD (Recursive)
# ---------------------------------------------------------------
def quicksort(array, low=0, high=None, depth=0):
    """
    Recursive Quicksort function.
    Splits array around pivot and sorts left/right sub-arrays.
    """
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)

        # Debug output for understanding
        indent = "  " * depth
        print(f"{indent}Pivot placed at index {pivot_index} → {array}")

        # Recursively sort left and right parts
        quicksort(array, low, pivot_index - 1, depth + 1)
        quicksort(array, pivot_index + 1, high, depth + 1)


# ---------------------------------------------------------------
# 4. DEMONSTRATION WITH SAMPLE LIST
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 2: QUICKSORT IMPLEMENTATION ")
print("==============================")

mylist = [64, 34, 25, 5, 22, 11, 90, 12]
print(f"Original List: {mylist}\n")

quicksort(mylist)  # Run quicksort
print(f"\n✅ Final Sorted List: {mylist}\n")

print("Important Notes:")
print("➡ Quicksort uses recursion: quicksort() calls itself for sub-arrays.")
print("➡ Partitioning ensures pivot is always in the correct position.")
print("➡ Sorting continues until sub-arrays are too small (size 0 or 1).\n")


# ---------------------------------------------------------------
# 5. TIME COMPLEXITY EXPLANATION
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 3: TIME COMPLEXITY ")
print("==============================")

print("🔹 Best Case: O(n log n) → When pivot splits array evenly each time.")
print("🔹 Average Case: O(n log n) → Random pivot distribution.")
print("🔹 Worst Case: O(n²) → When pivot is smallest/largest each time (e.g. already sorted).")

print("\nExamples:")
print("n = 10 → Best ≈ 30 steps | Worst ≈ 100 steps")
print("n = 100 → Best ≈ 660 steps | Worst ≈ 10,000 steps")

print("\n✅ Quicksort is usually much faster than Bubble/Insertion/Selection Sort.")
print("   That’s why Quicksort is widely used in practice.\n")

print("==============================")
print(" END OF QUICKSORT DEMO ")
print("==============================")

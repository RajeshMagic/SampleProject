# ==============================================================
# INSERTION SORT DEMONSTRATION IN PYTHON
# ==============================================================
# This program demonstrates:
#   1. Manual walkthrough of Insertion Sort
#   2. Basic Insertion Sort implementation (with shifting problem)
#   3. Improved Insertion Sort implementation (efficient shifting)
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
print("Step 1: Consider [7] as sorted part")
print("[7 | 12, 9, 11, 3]")

print("Step 2: Insert 12 → Already larger than 7 → [7, 12 | 9, 11, 3]")
print("Step 3: Insert 9 → Goes between 7 and 12 → [7, 9, 12 | 11, 3]")
print("Step 4: Insert 11 → Goes between 9 and 12 → [7, 9, 11, 12 | 3]")
print("Step 5: Insert 3 → Goes at front → [3, 7, 9, 11, 12]")

print("\n✅ Final Sorted Array: [3, 7, 9, 11, 12]")

print("\nImportant Note:")
print("➡ Insertion Sort builds the sorted part step by step,")
print("   inserting each new value into the correct position.\n")


# ---------------------------------------------------------------
# 2. BASIC INSERTION SORT (with shifting problem)
# ---------------------------------------------------------------
def insertion_sort_basic(arr):
    """
    Basic Insertion Sort using pop + insert.
    Works fine, but has hidden inefficiencies due to shifting.
    """
    n = len(arr)
    for i in range(1, n):
        insert_index = i
        current_value = arr.pop(i)  # Remove element
        for j in range(i - 1, -1, -1):
            if arr[j] > current_value:
                insert_index = j
        arr.insert(insert_index, current_value)  # Insert at correct position
        print(f"After inserting index {i}: {arr}")
    return arr


print("\n==============================")
print(" STEP 2: BASIC INSERTION SORT ")
print("==============================")

mylist = [64, 34, 25, 12, 22, 11, 90, 5]
print(f"Original List: {mylist}\n")

sorted_list_basic = insertion_sort_basic(mylist.copy())
print(f"\n✅ Final Sorted List: {sorted_list_basic}\n")

print("⚠️ Important Note:")
print("This version uses POP + INSERT which internally shifts many elements.")
print("That makes it less efficient when working with large lists.\n")


# ---------------------------------------------------------------
# 3. IMPROVED INSERTION SORT (efficient shifting)
# ---------------------------------------------------------------
def insertion_sort_improved(arr):
    """
    Improved Insertion Sort:
    Instead of pop + insert, we shift only necessary values
    and place the current value directly in its correct position.
    """
    n = len(arr)
    for i in range(1, n):
        current_value = arr[i]
        insert_index = i

        # Shift elements one step to the right
        for j in range(i - 1, -1, -1):
            if arr[j] > current_value:
                arr[j + 1] = arr[j]   # Shift right
                insert_index = j
            else:
                break  # No need to continue if current_value is larger

        arr[insert_index] = current_value
        print(f"After inserting index {i}: {arr}")
    return arr


print("\n==============================")
print(" STEP 3: IMPROVED INSERTION SORT ")
print("==============================")

mylist2 = [64, 34, 25, 12, 22, 11, 90, 5]
print(f"Original List: {mylist2}\n")

sorted_list_improved = insertion_sort_improved(mylist2.copy())
print(f"\n✅ Final Sorted List: {sorted_list_improved}\n")

print("✅ Important Note:")
print("This version avoids unnecessary shifting.")
print("Much faster when working with larger datasets.\n")


# ---------------------------------------------------------------
# 4. TIME COMPLEXITY
# ---------------------------------------------------------------
print("\n==============================")
print(" STEP 4: TIME COMPLEXITY ")
print("==============================")

print("🔹 Best Case: O(n) → Already sorted array (minimal shifts).")
print("🔹 Average Case: O(n²) → Random order (each element compared to many others).")
print("🔹 Worst Case: O(n²) → Reverse order (every element shifted each time).")
print("\nExample Comparisons:")
print("n = 10 → ~25 comparisons (avg)")
print("n = 100 → ~5,000 comparisons (avg)")
print("\n➡ Faster than Bubble/Selection Sort when array is nearly sorted.")
print("➡ But still not efficient for very large arrays.\n")

print("==============================")
print(" END OF INSERTION SORT DEMO ")
print("==============================")

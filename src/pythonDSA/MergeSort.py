"""
Merge Sort in Python
--------------------
This script demonstrates Merge Sort with detailed explanations.
It includes:
1. Recursive Merge Sort
2. Iterative (non-recursive) Merge Sort
3. Manual walk-through explanation via console outputs
4. Important Notes & Time Complexity

Author: Example DSA Script
"""

# -------------------------------
# Merge Function (common for both implementations)
def merge(left, right):
    """
    Merge two sorted lists into one sorted list.
    Keeps the order stable (important in sorting!).
    """
    result = []
    i = j = 0

    # Compare and append in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining values
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# -------------------------------
# Recursive Merge Sort
def merge_sort_recursive(arr):
    """
    Recursive Merge Sort implementation.
    Splits the array into halves until sub-arrays have one element,
    then merges them back together in sorted order.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive calls
    sorted_left = merge_sort_recursive(left_half)
    sorted_right = merge_sort_recursive(right_half)

    # Merge step
    return merge(sorted_left, sorted_right)


# -------------------------------
# Iterative Merge Sort
def merge_sort_iterative(arr):
    """
    Iterative (non-recursive) Merge Sort.
    Uses increasing step sizes to merge sub-arrays.
    """
    step = 1
    length = len(arr)

    while step < length:
        for i in range(0, length, 2 * step):
            left = arr[i:i + step]
            right = arr[i + step:i + 2 * step]

            merged = merge(left, right)

            # Place merged back into original array
            for j, val in enumerate(merged):
                arr[i + j] = val

        step *= 2
    return arr


# -------------------------------
# Demo function to explain manual steps
def manual_walkthrough():
    print("\n--- Manual Walkthrough of Merge Sort ---")
    arr = [12, 8, 9, 3, 11, 5, 4]
    print("Original Array:", arr)

    print("\nStep 1: Split array into two halves")
    print("[12, 8, 9] and [3, 11, 5, 4]")

    print("\nStep 2: Continue splitting")
    print("[12], [8, 9], [3, 11], [5, 4]")

    print("\nStep 3: Start merging smallest parts")
    print("Merge [8] and [9] → [8, 9]")
    print("Merge [5] and [4] → [4, 5]")

    print("\nStep 4: Merge intermediate parts")
    print("Merge [12] and [8, 9] → [8, 9, 12]")
    print("Merge [3, 11] and [4, 5] → [3, 4, 5, 11]")

    print("\nStep 5: Final merge")
    print("Merge [8, 9, 12] and [3, 4, 5, 11] → [3, 4, 5, 8, 9, 11, 12]")

    print("\n--- Manual walkthrough finished ---")


# -------------------------------
# Main Execution
if __name__ == "__main__":
    print("\n=== Merge Sort Demonstration ===")

    # Manual steps
    manual_walkthrough()

    # Example with recursive implementation
    mylist1 = [3, 7, 6, -10, 15, 23.5, 55, -13]
    print("\n--- Recursive Merge Sort ---")
    print("Original Array:", mylist1)
    sorted_list1 = merge_sort_recursive(mylist1)
    print("Sorted Array:", sorted_list1)

    # Example with iterative implementation
    mylist2 = [3, 7, 6, -10, 15, 23.5, 55, -13]
    print("\n--- Iterative Merge Sort ---")
    print("Original Array:", mylist2)
    sorted_list2 = merge_sort_iterative(mylist2)
    print("Sorted Array:", sorted_list2)

    # Important notes
    print("\n--- Important Notes on Merge Sort ---")
    print("1. Merge Sort is a Divide & Conquer algorithm.")
    print("2. It always splits the array into halves until 1 element remains.")
    print("3. Sub-arrays are then merged back in sorted order.")
    print("4. Merge Sort is STABLE (preserves relative order of equal elements).")
    print("5. Time Complexity: O(n log n) in best, average, and worst cases.")
    print("6. Space Complexity: O(n) because of temporary arrays during merging.\n")

"""
Radix Sort in Python
---------------------
This script demonstrates Radix Sort and its variations.
It explains important points with elaborate console output
so you can clearly understand how the algorithm works.
"""

# -------------------------------
# Utility function for printing arrays nicely
def print_array(arr, message="Array:"):
    print(f"{message} {arr}")


# -------------------------------
# Bubble Sort (to be used later inside Radix Sort)
def bubble_sort(arr):
    """
    Standard Bubble Sort algorithm.
    Time Complexity: O(n^2)
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# -------------------------------
# Radix Sort (using Buckets)
def radix_sort(arr):
    """
    Radix Sort using bucket-based approach.
    Sorts numbers digit by digit starting from Least Significant Digit (LSD).
    """
    print("\n--- Radix Sort Demonstration ---")
    print("Important Note: Radix Sort works only on non-negative integers and requires stable sorting.\n")
    print_array(arr, "Original Array:")

    max_val = max(arr)
    exp = 1  # 1 for units, 10 for tens, 100 for hundreds...

    # Loop until the largest digit place is covered
    while max_val // exp > 0:
        print(f"\nSorting by digit at place: {exp} (1=units, 10=tens, 100=hundreds, etc.)")

        # Buckets for each digit (0-9)
        buckets = [[] for _ in range(10)]

        # Distribute elements into buckets
        for num in arr:
            index = (num // exp) % 10
            buckets[index].append(num)

        print("Buckets after distribution:", buckets)

        # Collect back into array
        i = 0
        for bucket in buckets:
            for num in bucket:
                arr[i] = num
                i += 1

        print_array(arr, f"Array after sorting with digit place {exp}:")
        exp *= 10

    print("\nFinal Sorted Array (Radix Sort):", arr)
    print("Important Note: Stability ensures that numbers with the same digit maintain relative order.\n")
    return arr


# -------------------------------
# Radix Sort (using Bubble Sort for digit sorting)
def radix_sort_with_bubble(arr):
    """
    Radix Sort implemented using Bubble Sort to sort each digit.
    """
    print("\n--- Radix Sort with Bubble Sort Demonstration ---")
    print("Important Note: This version shows how Radix Sort can use a stable algorithm (Bubble Sort) for each digit.\n")
    print_array(arr, "Original Array:")

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        print(f"\nSorting by digit at place: {exp}")

        # Buckets for digits 0-9
        buckets = [[] for _ in range(10)]

        # Place numbers into buckets
        for num in arr:
            index = (num // exp) % 10
            buckets[index].append(num)

        print("Buckets before sorting each with Bubble Sort:", buckets)

        # Sort each bucket with Bubble Sort (ensures stability)
        for bucket in buckets:
            bubble_sort(bucket)

        print("Buckets after Bubble Sort:", buckets)

        # Rebuild array
        i = 0
        for bucket in buckets:
            for num in bucket:
                arr[i] = num
                i += 1

        print_array(arr, f"Array after sorting with digit place {exp}:")
        exp *= 10

    print("\nFinal Sorted Array (Radix with Bubble Sort):", arr)
    return arr


# -------------------------------
# Main Execution
if __name__ == "__main__":
    # Example 1: Normal Radix Sort
    mylist1 = [170, 45, 75, 90, 802, 24, 2, 66]
    radix_sort(mylist1.copy())

    # Example 2: Radix Sort with Bubble Sort
    mylist2 = [170, 45, 75, 90, 802, 24, 2, 66]
    radix_sort_with_bubble(mylist2.copy())

    # Important Notes about Complexity
    print("\n--- Important Notes on Radix Sort Complexity ---")
    print("1. Time Complexity: O(n * k), where n = number of elements, k = number of digits in the max number.")
    print("2. Best Case: O(n) if numbers are large but have few digits.")
    print("3. Worst Case: O(n^2) if number of digits is close to number of elements.")
    print("4. Most common scenario: O(n * log(n)) if digits ≈ log(n).")
    print("5. Radix Sort is non-comparative and stable, making it useful in some cases over Quick/Merge Sort.\n")

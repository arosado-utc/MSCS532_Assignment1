"""
MSCS 532 - Assignment 1
Assignment: Insertion Sort (monotonically decreasing order)
By: Alfredo Rosado
Date: 10-25-26

Reference: Based on Chapter 2 of Cormen, Leiserson, Rivest & Stein,
"Introduction to Algorithms" (4th ed., 2022).
"""

def decending_order_insert_sort(arr):
    """
    Function: Takes an array and sorts the array
    using insertion sort in decreasing order
    Parameter: arr
    Return: arr
    """
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        # Shift elements that are smaller than the key one slot right
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i -= 1
        # Place the key in its correct position
        arr[i + 1] = key
    return arr


def main():
    # A few sample lists to demonstrate the sort
    sample_arrays = [
        [12, 11, 13, 5, 6],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [4, 4, 2, 4, 1],
        [-3, 0, -7, 4, -1],
    ]

    for test in sample_arrays:
        original = list(test)
        print(f"Before: {original}")
        decending_order_insert_sort(test)
        print(f"After:  {test}")
        print()

if __name__ == "__main__":
    main()

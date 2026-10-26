"""
MSCS 532 - Assignment 1
Assignment: Insertion Sort (monotonically decreasing order)

Reference: Based on Chapter 2 of Cormen, Leiserson, Rivest & Stein,
"Introduction to Algorithms" (4th ed., 2022).
"""

def decending_order_insert_sort(arr):
    """
    Function: Takes an array sorts the array
    using insert sort in decending order
    Parameter: arr
    Return: arr
    """

    #Place Holder for algo
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
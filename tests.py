"""
Tests for decending_order_insert_sort in main.py.

Run with:  python3 tests.py
"""

from main import decending_order_insert_sort


def test_already_decreasing():
    """A list that is already sorted decreasing stays unchanged."""
    data = [9, 7, 5, 3, 1]
    decending_order_insert_sort(data)
    assert data == [9, 7, 5, 3, 1]


def test_increasing_input():
    """A list that is increasing must be fully reversed."""
    data = [1, 2, 3, 4, 5]
    decending_order_insert_sort(data)
    assert data == [5, 4, 3, 2, 1]


def test_duplicates():
    """Duplicate values must all be kept and ordered correctly."""
    data = [4, 4, 2, 4, 1]
    decending_order_insert_sort(data)
    assert data == [4, 4, 4, 2, 1]


def test_negative_numbers():
    """Negative numbers sort relative to each other (e.g. -1 > -9)."""
    data = [-1, -9, -3, -5]
    decending_order_insert_sort(data)
    assert data == [-1, -3, -5, -9]


def test_single_element_and_empty():
    """Edge cases: a list with one item and an empty list."""
    single = [42]
    decending_order_insert_sort(single)
    assert single == [42]

    empty = []
    decending_order_insert_sort(empty)
    assert empty == []


def test_matches_builtin_sorted():
    """The result must agree with Python's built-in sorted(reverse=True)."""
    data = [7, 2, 9, 0, 5, 8, 3]
    decending_order_insert_sort(data)
    assert data == sorted(data, reverse=True)


def test_two_elements():
    """The smallest non-trivial list must be ordered correctly."""
    data = [1, 2]
    decending_order_insert_sort(data)
    assert data == [2, 1]


def test_floats():
    """Decimal (float) values must sort like integers."""
    data = [0.5, 3.2, -1.7, 2.0]
    decending_order_insert_sort(data)
    assert data == [3.2, 2.0, 0.5, -1.7]


def test_all_identical():
    """A list where every value is the same must stay unchanged."""
    data = [7, 7, 7, 7]
    decending_order_insert_sort(data)
    assert data == [7, 7, 7, 7]


def test_mixed_zeros():
    """Zeros must land between the positive and negative values."""
    data = [0, -2, 3, 0, -1]
    decending_order_insert_sort(data)
    assert data == [3, 0, 0, -1, -2]


def test_longer_list():
    """A longer list (15 elements) must agree with sorted(reverse=True)."""
    data = [23, 7, 19, 2, 11, 34, 5, 8, 29, 14, 1, 17, 3, 26, 12]
    decending_order_insert_sort(data)
    assert data == sorted(data, reverse=True)


def main():
    tests = [
        test_already_decreasing,
        test_increasing_input,
        test_duplicates,
        test_negative_numbers,
        test_single_element_and_empty,
        test_matches_builtin_sorted,
        test_two_elements,
        test_floats,
        test_all_identical,
        test_mixed_zeros,
        test_longer_list,
    ]

    failed = 0
    for test in tests:
        try:
            test()
            print(f"PASS: {test.__name__}")
        except AssertionError:
            failed += 1
            print(f"FAIL: {test.__name__}")

    print()
    if failed:
        print(f"{failed} of {len(tests)} test(s) FAILED.")
        raise SystemExit(1)
    print(f"All {len(tests)} tests passed.")


if __name__ == "__main__":
    main()

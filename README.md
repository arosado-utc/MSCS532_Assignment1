# MSCS532 Assignment 1: Insertion Sort (Decreasing)

Python implementation of the **Insertion Sort** algorithm from
Cormen, Leiserson, Rivest & Stein, *Introduction to Algorithms*
(4th ed., 2022), Chapter 2.

The standard textbook version sorts a list in **increasing** order. This
assignment requires sorting in **monotonically decreasing** order (largest
to smallest), so the comparison in the inner loop is flipped.

## Requirements

- Python 3.8 or higher

## Files

| File        | Description                                          |
| ----------- | ---------------------------------------------------- |
| `main.py`   | Insertion sort (decreasing) algorithm + small demo   |
| `tests.py`  | Test suite that verifies the sort behaves correctly  |

## How to run

Run the demo:

```bash
python3 main.py
```

Run the tests:

```bash
python3 tests.py
```

## How it works

Insertion Sort builds the sorted list one element at a time. Starting at
index 1, each element ("the key") is inserted into its correct position in
the already-sorted prefix to its left by shifting elements one slot to the
right.

To sort **decreasing** instead of increasing, the inner loop shifts while
the element on the left is **smaller** than the key (`arr[i] < key`),
instead of **larger** (`arr[i] > key`):

```python
for j in range(1, len(arr)):
    key = arr[j]
    i = j - 1
    while i >= 0 and arr[i] < key:   # <-- flipped comparison
        arr[i + 1] = arr[i]
        i -= 1
    arr[i + 1] = key
```

## Complexity

- **Time:** O(n²) worst and average case, O(n) best case (already sorted)
- **Space:** O(1) — sorts in place
- **Stable:** yes

## Reference

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022).
*Introduction to Algorithms* (4th ed.). Random House Publishing Services.
https://reader2.yuzu.com/books/9780262367509

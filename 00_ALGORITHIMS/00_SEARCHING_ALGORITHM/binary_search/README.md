### Binary Search

Given a sorted `list` of numbers or items a binary search algorithm search a sorted list by repeatedly dividing the search interval in half. Begin with an interval covering the whole array.

If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half.
Otherwise, narrow it to the upper half.
Repeatedly check until the value is found or the interval is empty.

### Algorithm Steps

1. Compare target with the middle element.
2. If target matches with the middle element, we return the mid index.
3. Else If target is greater than the mid element, then target can only lie in the right half sub-array after the mid element.
4. Else (x is smaller) recur for the left half.

### Implementation 1

The piece of code bellow shows the implementation of the binary search algorithm using the `iterative approach`.

```py
def binary_search(elements:list, target:int)->int:
    first = 0
    last = len(elements) - 1
    while first <= last:
        mid = (first + last) // 2
        if elements[mid] == target:
            return mid
        elif elements[mid] < target:
            first = mid + 1
        elif elements[mid] > target:
            last = mid - 1
    return -1

# Testing the Algorithm
numbers = [i for i in range(10)]

assert binary_search(numbers, 6) == 6, "The element was not found."
assert binary_search(numbers, 10) == -1, "The element was not found"
```

### Implementation 2 (Recursive approach)

We can implement the binary search using what we call the `recursive` approach and python list slicing. This is more efficient in terms of storage but in some languages because in python when the list is very big it will run into a `recursive depth` exception which is the number of times the function called itself:

> A **Recursive function** is a function that called itself in it's body.

```py


def binary_search(elements:list, target:int, start:int =0, end=None)->int:
    if end is None:
        end = len(elements) -1
    if start > end:return -1
    mid = (start + end)//2

    if elements[mid] == target:
        return mid
    elif elements[mid] < target:
        return binary_search(elements, target, mid+1, end)
    else:
        return binary_search(elements, target, start, mid-1)

# Testing the Algorithm
numbers = [i for i in range(10)]

assert binary_search(numbers, 6) == 6, "The element was not found."
assert binary_search(numbers, 10) == -1, "The element was not found"
```

### Algorithm Efficiency

- The time complexity of Binary Search can be written as:

```
T(n) = T(n/2) + c
```

The time complexity of the binary search algorithm is **O(log n)** or **O(ln n)**.

### Disadvantages of binary search

Binary search only works efficiently on sorted collections, this brings a limitation that we have to sort the list first.

### Advantages of the binary search Algo

The binary search is much faster as compared to the linear search algorithm.

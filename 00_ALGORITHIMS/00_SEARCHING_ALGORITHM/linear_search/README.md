### Linear Search

Given a `list` of numbers or items a linear search algorithm searches for an element in sequence and return an `index` of the element when found otherwise it returns any value like `None`, `-1`, etc to indicate that the element is not found.

### Algorithm Steps

1. Start from the most left side of a list
2. Compare the target value with the current value at an `index`.
3. If the value is found at a certain `index` we return that index otherwise we return a `-1`.

### Implementation 1

The piece of code bellow shows the implementation of the liner search algorithm.

```py

def linear_search(elements:list, target:int)->int:
    for index in range(0, len(elements)):
        if elements[index] == target:
            """
            if the element if found we return the index of the element
            """
            return index
    """
    If the element is not found we return a nagative index
    """
    return -1

# Testing the algorithim
numbers = [i for i in range(10)]

assert linear_search(numbers, 6) == 6, "The element was not found."
assert linear_search(numbers, 10) == -1, "The element was not found"

```

### Implementation 2 (using `enumerate`)

This is a shorter method of implementing a linear search algorithm in python:

```py

def linear_search(elements:list, target:int)->int:
    for index, item in enumerate(elements):
        if item == target: return index
    return -1

# Testing the algorithim
numbers = [i for i in range(10)]

assert linear_search(numbers, 6) == 6, "The element was not found."
assert linear_search(numbers, 10) == -1, "The element was not found"

```

### Algorithm Efficiency

- Efficiency of an algorithm is measured when the algorithm performs it's task successfully.
- Algorithm efficiency is measured using in terms of:
  - **time complexity**
  - **space complexity**
- Time complexity of an algorithm is measured using **The Big O Notation**

The time complexity of **linear search** algorithm is **O(n)**.

### The Best Case of the Linear Search Algorithm

Consider we have a list where the target(element we are looking for) is at the first index of the list. This is considered as the best case because the time complexity of the algorithm will be **`O(1)`**

> **`O(1)`** is a constant time complexity of an algorithm a good example of **`O(1)`** are assignment and comparison operations.

### The Worst Case of the Linear Search Algorithm

Consider we have a list where the target(element we are looking for) is at the last index of the list. This is considered as the worst case snerio because the time complexity of the algorithm will be **`O(n)`**

### Advantages of the linear search Algo

- Elements must to not be sorted in any order unlike in `binary search`
- Easy to implement

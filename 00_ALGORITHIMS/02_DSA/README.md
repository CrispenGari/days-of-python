### Algorithms in Python

In this notebook we are going to have a look at how to implement some algorithms in python. Here are some of the algorithms categories that we are going to implement:

1. **Math Algorithms**
2. **Recursion Algorithms**
3. **Searching Algorithm**
4. **Sorting Algorithm**
5. **Miscellaneous Algorithms**

### Time and Space Complexity Cheat-Sheet.

The following table contains a cheat-sheet for time complexity and space complexity for the `Big-O` notations of code expressions.

| Description                                 | Big-O notation | Type          |
| ------------------------------------------- | -------------- | ------------- |
| Alignment operations and conditional checks | `O(1)`         | `Constant`    |
| Loops                                       | `O(n)`         | `Linear`      |
| 2 Nested loops                              | `O(n^2)`       | `Quadratic`   |
| Loops that reduces by half in the body      | `O(log(n))`    | `Logarithmic` |

Let's start by implementing the Math Algorithmns.

### Math Algorithms

In this section we are going to implement some mathematical algorithms identify their time complexity and optimize them where necessary. These algorithmns include:

1. Factorial
2. Fibonacci Serries
3. Prime
4. Power of 2

#### 1. factorial

A factorial of a number (`n`) is product of the numbers starting from `1` to `n`.

```python
def factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

print("1 factorial: ", factorial(1))
print("2 factorial: ", factorial(2))
print("3 factorial: ", factorial(3))
print("4 factorial: ", factorial(4))
print("5 factorial: ", factorial(5))
```

**Output:**

```text
1 factorial:  1
2 factorial:  2
3 factorial:  6
4 factorial:  24
5 factorial:  120
```

- Time complexity: **O(n)**

#### 2. Fibonacci Serries

This is a serries of numbers in which the next number is obtained by adding the 2 previous numbers in the series.

```python
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

print("fibonacci of 1: ", fibonacci(1))
print("fibonacci 2: ", fibonacci(2))
print("fibonacci 3: ", fibonacci(3))
print("fibonacci 4: ", fibonacci(4))
print("fibonacci 5: ", fibonacci(5))
```

**Output:**

```text
fibonacci of 1:  [0, 1]
fibonacci 2:  [0, 1]
fibonacci 3:  [0, 1, 1]
fibonacci 4:  [0, 1, 1, 2]
fibonacci 5:  [0, 1, 1, 2, 3]
```

- Time complexity: **O(n)**

#### 2. prime

A prime number `n` is a number that have oly two factors, which are `1` and `n`.

```python
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(10):
    print(f"isPrime({i}): ", isPrime(i))
```

**Output:**

```text
isPrime(0):  False
isPrime(1):  False
isPrime(2):  True
isPrime(3):  True
isPrime(4):  False
isPrime(5):  True
isPrime(6):  False
isPrime(7):  True
isPrime(8):  False
isPrime(9):  False
```

- Time complexity: **O(n)**

> Integers larger than the square root do not need to be checked for prime because whenever `n=a*b`, one of the two factors `a` and `b` is less than or equal to the square root of `n`

- The above algorithm can be optimized or improved as follows.

```python
import math
def isPrime(n):
    if n < 2:
        return False
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i+=1
    return True

for i in range(10):
    print(f"isPrime({i}): ", isPrime(i))
```

**Output:**

```text
isPrime(0):  False
isPrime(1):  False
isPrime(2):  True
isPrime(3):  True
isPrime(4):  False
isPrime(5):  True
isPrime(6):  False
isPrime(7):  True
isPrime(8):  False
isPrime(9):  False
```

- Time complexity: **O(sqrt(n))**

#### 3. powerOfTwo

We want to determine given an integer value `n` if `n` is a power of 2.

```python
def powerOfTwo(n):
    if n < 1:
        return False
    while n > 1:
        if n % 2 != 0:
            return False
        n /= 2
    return True
for i in range(17):
    print(f"powerOfTwo({i}): ", powerOfTwo(i))
```

**Output:**

```text
powerOfTwo(0):  False
powerOfTwo(1):  True
powerOfTwo(2):  True
powerOfTwo(3):  False
powerOfTwo(4):  True
powerOfTwo(5):  False
powerOfTwo(6):  False
powerOfTwo(7):  False
powerOfTwo(8):  True
powerOfTwo(9):  False
powerOfTwo(10):  False
powerOfTwo(11):  False
powerOfTwo(12):  False
powerOfTwo(13):  False
powerOfTwo(14):  False
powerOfTwo(15):  False
powerOfTwo(16):  True
```

- Time complexity: **O(log(n))**
- The above algorithm can be improved as follows

```python
def powerOfTwo(n):
    if n < 1:
        return False
    return n & (n - 1) == 0

for i in range(17):
    print(f"powerOfTwo({i}): ", powerOfTwo(i))
```

**Output:**

```text
powerOfTwo(0):  False
powerOfTwo(1):  True
powerOfTwo(2):  True
powerOfTwo(3):  False
powerOfTwo(4):  True
powerOfTwo(5):  False
powerOfTwo(6):  False
powerOfTwo(7):  False
powerOfTwo(8):  True
powerOfTwo(9):  False
powerOfTwo(10):  False
powerOfTwo(11):  False
powerOfTwo(12):  False
powerOfTwo(13):  False
powerOfTwo(14):  False
powerOfTwo(15):  False
powerOfTwo(16):  True
```

- Time complexity: **O(1)**

### Recursion Algorithms

A recursive function is a function that calls itself in the function body. Let's have a look at some of the examples.

> Note: Every recessive function should have a base case, which controls the termination of a function otherwise an infinite loop will arise.

#### 1. factorial problem

We are going to approach the factorial problem to find a factorial of `n` which is a positive integer greater than 0 using recursion.

```python
def factorial(n):
    if n < 2: return 1
    return n * factorial(n -1)

for i in range(8):
    print(f"factorial({i}): ", factorial(i))
```

**Output:**

```text
factorial(0):  1
factorial(1):  1
factorial(2):  2
factorial(3):  6
factorial(4):  24
factorial(5):  120
factorial(6):  720
factorial(7):  5040
```

- Time complexity: **O(n)**

  > We can conclude that using iterative approach is the same as using the recursive approach in solving factorial problem.

#### 2. fibonacci problem

Let's use the recursive approach to find the `nth` fibonacci term

```python
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n -1) + fibonacci(n-2)

for i in range(8):
    print(f"fibonacci({i}): ", fibonacci(i))
```

**Output:**

```text
fibonacci(0):  0
fibonacci(1):  1
fibonacci(2):  1
fibonacci(3):  2
fibonacci(4):  3
fibonacci(5):  5
fibonacci(6):  8
fibonacci(7):  13
```

- Time complexity: **O(2^n)**
  > We can conclude that using iterative approach is better than using recessive approach when solving the fibonacci problem.

### Searching Algorithm

In this section we are going to have a look at how we can implement some searching algorithms in typescript.

#### 1. Linear Search

Given an array of numbers and a target element return the index of that element or `-1` if the element does not exists in an array. Here is how we can go about it:

1. loop through elements in an array and compare if the element matches the element at that particular index
2. if it does return the index of that element
3. if the element was not found return `-1`

```python
def linearSearch(array, ele):
    for i, val in enumerate(array):
        if ele == val:
            return i
    return -1

elements = list(range(6))

for i in range(10):
    print(f"linearSearch({elements, i}): ", linearSearch(elements, i))
```

**Output:**

```text
linearSearch(([0, 1, 2, 3, 4, 5], 0)):  0
linearSearch(([0, 1, 2, 3, 4, 5], 1)):  1
linearSearch(([0, 1, 2, 3, 4, 5], 2)):  2
linearSearch(([0, 1, 2, 3, 4, 5], 3)):  3
linearSearch(([0, 1, 2, 3, 4, 5], 4)):  4
linearSearch(([0, 1, 2, 3, 4, 5], 5)):  5
linearSearch(([0, 1, 2, 3, 4, 5], 6)):  -1
linearSearch(([0, 1, 2, 3, 4, 5], 7)):  -1
linearSearch(([0, 1, 2, 3, 4, 5], 8)):  -1
linearSearch(([0, 1, 2, 3, 4, 5], 9)):  -1
```

- Time complexity: **O(n)**

#### 2. Binary Search

Given an **sorted** array of elements, find the index of the element in an array and return `-1` if the element does not exists in an array. Here is how the binary search algorithm works.

##### 2.1 Iterative approach

1. find the first and last index
2. if the first and last index are equal return `-1`
3. find the middle index by rounding down the sum of `first` and `last` index after dividing them by `2`.
4. check if the middle element is greater than the element:
   - if it is this means the element is on the left half
     - update the right index to middle index less 1
   - if not this means the element is on the right half
     - update the left index to middle index plus 1

> Note that `Binary Search` algorithm works on sorted arrays.

```python
def search(array, ele, left, right):
    mid = (left + right)//2
    if left > right:
        return -1
    if array[mid] == ele:
        return mid
    if array[mid] > ele:
       # the element is on the left half
        return search(array, ele, left, mid - 1)
    else:
        # the element is on the right half
        return search(array, ele, mid + 1, right);
def binarySearch(array, ele):
    return search(array, ele, 0, len(array) - 1)

elements = list(range(6))

for i in range(10):
    print(f"binarySearch({elements, i}): ", binarySearch(elements, i))
```

**Output:**

```text
binarySearch(([0, 1, 2, 3, 4, 5], 0)):  0
binarySearch(([0, 1, 2, 3, 4, 5], 1)):  1
binarySearch(([0, 1, 2, 3, 4, 5], 2)):  2
binarySearch(([0, 1, 2, 3, 4, 5], 3)):  3
binarySearch(([0, 1, 2, 3, 4, 5], 4)):  4
binarySearch(([0, 1, 2, 3, 4, 5], 5)):  5
binarySearch(([0, 1, 2, 3, 4, 5], 6)):  -1
binarySearch(([0, 1, 2, 3, 4, 5], 7)):  -1
binarySearch(([0, 1, 2, 3, 4, 5], 8)):  -1
binarySearch(([0, 1, 2, 3, 4, 5], 9)):  -1
```

? What if elements are sorted in descending order?

1. if not we check if the middle element is less than element
   - if this condition sets then which means the element is on the left half
     - we recursively call the `search` with the right index updated
   - else this means that the element is on the right half.
     - we recursively call the `search` with the left index updated.

```python
def search(array, ele, left, right):
    mid = (left + right)//2
    if left > right:
        return -1
    if array[mid] == ele:
        return mid
    if array[mid] < ele:
       # the element is on the left half
        return search(array, ele, left, mid - 1)
    else:
        # the element is on the right half
        return search(array, ele, mid + 1, right);
def binarySearch(array, ele):
    return search(array, ele, 0, len(array) - 1)

elements = list(range(6))[::-1]

for i in range(10):
    print(f"binarySearch({elements, i}): ", binarySearch(elements, i))
```

**Output:**

```text
binarySearch(([5, 4, 3, 2, 1, 0], 0)):  5
binarySearch(([5, 4, 3, 2, 1, 0], 1)):  4
binarySearch(([5, 4, 3, 2, 1, 0], 2)):  3
binarySearch(([5, 4, 3, 2, 1, 0], 3)):  2
binarySearch(([5, 4, 3, 2, 1, 0], 4)):  1
binarySearch(([5, 4, 3, 2, 1, 0], 5)):  0
binarySearch(([5, 4, 3, 2, 1, 0], 6)):  -1
binarySearch(([5, 4, 3, 2, 1, 0], 7)):  -1
binarySearch(([5, 4, 3, 2, 1, 0], 8)):  -1
binarySearch(([5, 4, 3, 2, 1, 0], 9)):  -1
```

- Time complexity: **O(log(n))**

### Sorting Algorithm

In this section we are going to look at some sorting algorithms.

#### 1. Bubble Sort

Given an array of numbers we want to sort them in `ascending` order. Here is how we can do it using the `bubbleSort` algorithm.

1. Keep in track of elements being swapped or not
2. Repeat the loop till swapped value is false
3. If the `left` element is greater than the `right` element we swap the two elements and set the `swapped` to `true`.

```python
def bubbleSort(ele):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ele) -1):
            if ele[i] > ele[i + 1]:
                ele[i], ele[i + 1] = ele[i+1], ele[i]
                # temp = ele[i]
                # ele[i] = ele[i + 1]
                # ele[i + 1] = temp
                swapped = True

elements = [3, -1, 8, 8, 7, 1, 10, -6]
print(f"{elements}")
bubbleSort(elements)
print(f"{elements}")
```

**Output:**

```text
[3, -1, 8, 8, 7, 1, 10, -6]
[-6, -1, 1, 3, 7, 8, 8, 10]
```

Here is the implementation that allows us to order elements in descending order using the `bubbleSort`.

1. If the `left` element is less than the `right` element we swap the two elements and set the `swapped` to `true`.

```python
def bubbleSort(ele):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ele) -1):
            if ele[i] < ele[i + 1]:
                ele[i], ele[i + 1] = ele[i+1], ele[i]
                swapped = True

elements = [3, -1, 8, 8, 7, 1, 10, -6]
print(f"{elements}")
bubbleSort(elements)
print(f"{elements}")
```

**Output:**

```text
[3, -1, 8, 8, 7, 1, 10, -6]
[10, 8, 8, 7, 3, 1, -1, -6]
```

#### 2. Insertion Sort

Having an array of numbers we want to sort the numbers in either descending or ascending order. Here is how the insertion sort works.

1. The array is split into two arrays a sorted and unsorted array.
2. We assume that the first element in the array is sorted.
3. Select an element in an unsorted array and compare it with the sorted part.
4. If the elements in the sorted array is smaller than the selected we proceed to the next element in the unsorted array else we shift the elements in the sorted part towards the right
5. We insert the selected element at the right index.
6. We repeat the above steps till all the elements are sorted. Let's consider the following visualization.

| -                 | -          | -          |                                     |
| ----------------- | ---------- | ---------- | ----------------------------------- |
| `[-6 20 8 -2 4]`  | `NTI` = 20 | `SE` = -6  | -6 > 20? NO : place 20 to the right |
| `[-6 20 8 -2 4]`  | `NTI` = 8  | `SE` = 20  | 20> 8? YES : Shift 20 the right     |
| `[-6 20 20 -2 4]` | `NTI` = 8  | `SE` = -6  | -6> 8? NO : place 8 the right       |
| `[-6 8 20 -2 4]`  | `NTI` = -2 | `SE` = -20 | 20> -2? YES : Shift 20 to the right |
| `[-6 8 20 20 4]`  | `NTI` = -2 | `SE` = 8   | 8> -2? YES : Shift 8 to the right   |
| `[-6 8 8 20 4]`   | `NTI` = -2 | `SE` = -6  | -6> -2? YES : Shift -6 to the right |
| `[-6 -2 8 20 4]`  | `NTI` = -2 | `SE` = -6  | -6> -2? No : place -2 to the right  |
| `[-6 -2 8 20 4]`  | `NTI` = 4  | `SE` = 20  | 20> 4? Yes : Shift 20 to the right  |
| `[-6 -2 8 20 20]` | `NTI` = 4  | `SE` = 8   | 8> 4? Yes : Shift 8 to the right    |
| `[-6 -2 8 8 20]`  | `NTI` = 4  | `SE` = -2  | -2> 4? No : place 4 to the right    |
| `[-6 -2 4 8 20]`  | -          | -          | -                                   |

- `NTI` - Number to insert.
- `SE` - Sorted element.

> Finally we will have a sorted array `[-6 -2 4 8 20]`. Now let's go and implement this:

```python
def insertionSort(arr):
    for i in range(1, len(arr)):
        nti = arr[i]
        j = i -1
        while j >= 0 and arr[j] > nti:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = nti

elements = [3, -1, 8, 8, 7, 1, 10, -6]
print(f"{elements}")
insertionSort(elements)
print(f"{elements}")
```

**Output:**

```text
[3, -1, 8, 8, 7, 1, 10, -6]
[-6, -1, 1, 3, 7, 8, 8, 10]
```

? What about sorting in descending order?

```python
def insertionSort(arr):
    for i in range(1, len(arr)):
        nti = arr[i]
        j = i -1
        while j >= 0 and arr[j] < nti:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = nti

elements = [3, -1, 8, 8, 7, 1, 10, -6]
print(f"{elements}")
insertionSort(elements)
print(f"{elements}")
```

**Output:**

```text
[3, -1, 8, 8, 7, 1, 10, -6]
[10, 8, 8, 7, 3, 1, -1, -6]
```

- Time complexity: **O(n^2)**

#### 3. Quick Sort

- When doing a quicksort first we need to pick up the pivot element.
  - **How do we pick up a pivot?.**
    - first element of an array
    - last element of an array
    - median value as pivot
    - random element as pivot
- When sorting with this algorithm we basically put everything that is smaller than the pivot to the left and to the right if greater.
- we repeat the process till we have an array of length 1. which is sorted by definition.

```python
def quickSort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) - 1]
    left = []
    right = []
    for i in range(len(arr)-1):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
              right.append(arr[i])
    return quickSort(left) + [pivot] + quickSort(right)

elements = [3, -1, 8, 8, 7, 1, 10, -6]
print(f"{elements}")
elements = quickSort(elements)
print(f"{elements}")
```

**Output:**

```text
[3, -1, 8, 8, 7, 1, 10, -6]
[-6, -1, 1, 3, 7, 8, 8, 10]
```

The above function returns a sorted array. If we want to sort arrays in place we can do it as follows:

```python
def swap(arr, i , j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, right)
    return i + 1

def quickSort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quickSort(arr, left, pivot - 1)
        quickSort(arr, pivot + 1, right)

elements = [3, -1, 8, 8, 7, 1, 10, -6]
print(f"{elements}")
quickSort(elements, 0, len(elements)-1)
print(f"{elements}")
```

**Output:**

```text
[3, -1, 8, 8, 7, 1, 10, -6]
[-6, -1, 1, 3, 7, 8, 8, 10]
```

? What about sorting in descending order?

```python
def quickSort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) - 1]
    left = []
    right = []
    for i in range(len(arr)-1):
        if arr[i] > pivot:
            left.append(arr[i])
        else:
              right.append(arr[i])
    return quickSort(left) + [pivot] + quickSort(right)

elements = [3, -1, 8, 8, 7, 1, 10, -6]
print(f"{elements}")
elements = quickSort(elements)
print(f"{elements}")
```

**Output:**

```text
[3, -1, 8, 8, 7, 1, 10, -6]
[10, 8, 8, 7, 3, 1, -1, -6]
```

To sort in descending order in place you just need to modify the `partition` to:

```python
def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] > pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, right)
    return i + 1

def quickSort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quickSort(arr, left, pivot - 1)
        quickSort(arr, pivot + 1, right)

elements = [3, -1, 8, 8, 7, 1, 10, -6]
print(f"{elements}")
quickSort(elements, 0, len(elements)-1)
print(f"{elements}")
```

**Output:**

```text
[3, -1, 8, 8, 7, 1, 10, -6]
[10, 8, 8, 7, 3, 1, -1, -6]
```

- Time complexity: **O(n^2)**

#### 4. Merge Sort

The merge sort works as follows

1. We divide the array into sub arrays with only one element which is considered sorted.
2. We will then merge them together

```python

def merge(left, right):
    sorted = []
    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            sorted.append(left[0])
            left = left[1:]
        else:
            sorted.append(right[0])
            right = right[1:]
    return sorted + left + right

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    return merge(mergeSort(left), mergeSort(right))

elements = [3, -1, 8, 8, 7, 1, 10, -6]
print(f"{elements}")
elements =mergeSort(elements)
print(f"{elements}")
```

**Output:**

```text
[3, -1, 8, 8, 7, 1, 10, -6]
[-6, -1, 1, 3, 7, 8, 8, 10]
```

? What about sorting in descending order?

```python
def merge(left, right):
    sorted = []
    while len(left) != 0 and len(right) != 0:
        if left[0] >= right[0]:
            sorted.append(left[0])
            left = left[1:]
        else:
            sorted.append(right[0])
            right = right[1:]
    return sorted + left + right

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    return merge(mergeSort(left), mergeSort(right))

elements = [3, -1, 8, 8, 7, 1, 10, -6]
print(f"{elements}")
elements =mergeSort(elements)
print(f"{elements}")
```

**Output:**

```text
[3, -1, 8, 8, 7, 1, 10, -6]
[10, 8, 8, 7, 3, 1, -1, -6]
```

- Time complexity: **O(n.log(n))**

#### 5. Stalin Sort

This is a sorting algorithm where an element that us not in order is removed from the list. The elements that are not sorted are moved to the start of the list in the order that they have appeared in the list. This process is repeated until the list is sorted.

```python
def stalinSort(arr):
    j = 0
    while True:
        moved = 0
        for i in range(len(arr) - 1 - j):
            if arr[i] > arr[i + 1]:
                index = arr[i]
                temp = arr[i + 1]

                # Remove the elements and reinsert them at the correct position
                arr.pop(i)
                arr.insert(i, temp)
                arr[i] = temp

                arr.pop(i + 1)
                arr.insert(i + 1, index)
                arr[i + 1] = index

                moved += 1
        j += 1
        if moved == 0:
            break
    return arr

elements = [3, -1, 8, 8, 7, 1, 10, -6]
print(f"{elements}")
elements = stalinSort(elements)
print(f"{elements}")
```

**Output:**

```text
[3, -1, 8, 8, 7, 1, 10, -6]
[-6, -1, 1, 3, 7, 8, 8, 10]
```

- Time complexity: **O(n^2)**

### Miscellaneous

In this section we are going to have a look at some miscellaneous algorithms.

#### 1. Cartesian Product

Given 2 finite non-empty sets find their **Cartesian Product**.

Let's say we have sets `A =[1, 2]` and `B = [1, 2, 3]` their Cartesian Product is `AxB = [[1, 2], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3]]`

```python
def cartesianProduct(a, b):
    cp = []
    for i in a:
        for j in b:
            cp.append([i, j])
    return cp
A =[1, 2]
B = [1, 2, 3]

cartesianProduct(A, B)
```

**Output:**

```text
[[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3]]
```

- Time complexity: **O(mn)** - depends on the length of set `A` and `B`

#### 2. Climbing Stairs

Given a staircase of `n` find the number of distinct ways to climb to the top. You can either climb 1 step or 2 steps at a time.

```shell
n = 1 -> [(1)]
n = 2 -> [(1), (2)]
n = 3 -> [(1, 1, 1), (1, 2), (2, 1)]
n = 4 -> [(1, 1, 1, 1), (1, 2, 1), (1 , 1, 2), (2, 1, 1), (2, 2)]
```

We can see from the patten that the number of ways we are getting by adding the `2` previous values eg:

```shell
n = 4 -> 2 + 3
n = 3 -> 2 + 1
```

Where our base case is `1` and `2`

```python
def climbingStaircase(n):
    steps = [1, 2]
    for i in range(2, n+1):
        steps.append(steps[i - 1] + steps[i - 2])
    return steps[n -1]

for i in range(1, 6):
    print(f"Climbing {i} steps can be done in {climbingStaircase(i)} way(s).")
```

**Output:**

```text
Climbing 1 steps can be done in 1 way(s).
Climbing 2 steps can be done in 2 way(s).
Climbing 3 steps can be done in 3 way(s).
Climbing 4 steps can be done in 5 way(s).
Climbing 5 steps can be done in 8 way(s).
```

We can do this with recursion as follows:

```python
def climbingStaircase(n):
    if (n < 3):
        return n
    return climbingStaircase(n - 1) + climbingStaircase(n - 2)

for i in range(1, 6):
    print(f"Climbing {i} steps can be done in {climbingStaircase(i)} way(s).")
```

**Output:**

```text
Climbing 1 steps can be done in 1 way(s).
Climbing 2 steps can be done in 2 way(s).
Climbing 3 steps can be done in 3 way(s).
Climbing 4 steps can be done in 5 way(s).
Climbing 5 steps can be done in 8 way(s).
```

- Time complexity: **O(n)**

#### 3. Tower of Hanoi

The goal is to move the entire stuck from the first rod to the last one abiding the following rules:

1. Only one disk can be moved
2. You only take the upper disk and place it on top of a smaller disk and on an empty rod.
3. No disk should be placed on top of the smaller disk.

**Procedure**

1. Shift `n-1` disk from `A` to `B` using `C` when required.
2. Shift the last disk from `A` to `C`
3. Shift `n-1` disk from `B` to `C` using `A` when required.
4. repeat the process

```python
def towerOfHanoi(disks, _from, to, using):
    if disks == 1:
        print(f"✔️ Move 💿 {disks} from {_from} to {to}.")
        return
    towerOfHanoi(disks - 1, _from, using, to);
    print(f"✔️ Move 💿 {disks} from {_from} to {to}.");
    towerOfHanoi(disks - 1, using, to, _from);

towerOfHanoi(3, "A", "C", "B")
```

**Output:**

```text
✔️ Move 💿 1 from A to C.
✔️ Move 💿 2 from A to B.
✔️ Move 💿 1 from C to B.
✔️ Move 💿 3 from A to C.
✔️ Move 💿 1 from B to A.
✔️ Move 💿 2 from B to C.
✔️ Move 💿 1 from A to C.
```

- Time complexity: **O(2^n)**

### Algorithm Design Techniques and Terminologies

1. **Brute force** - Simple and exhaustive technique that evaluate every possible outcome to find the best. e.g (Linear Search Algorithm)
2. **Greedy** - Choose the best option at that current time without considering the future e.g (Dijkstra's algorithm, Prim's algorithm and Kruskai's Algorithm)
3. **Divide and Conquer** - Divide a problem into smaller problem and each smaller problem will be solved and the partial solutions are then combined as a single solution. eg (Binary Search, Quick Sort, Merge Sort and Tower of hanoi)
4. **Dynamic Programming** - Divide the problem into smaller sub problems, breaking it down into smaller sub problem. Store the result and reuse it into sub problems. This is called a memorization and optimization technique that improves the time complexity of an algorithm. eg (Fibonacci and Climbing staircase)
5. **Backtracking** - Generates all possible solutions, check if the solution satisfies all the given constraints and only then you proceed with generating subsequent solutions. If the constraints are not satisfied backtrack and go on different path to find the solution. eg (N-Queens) problem.

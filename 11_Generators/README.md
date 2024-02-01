### Generators

Generators simplifies creation of iterators. A generator is a function that produces a sequence of results instead of a single value.

> So a generator is also an iterator.

#### A simple generator

```python
def y_range(n:int):
    while n > 0:
        yield n
        n-=1

a = y_range(10)
print(a) # <generator object y_range at 0x0000022CDF411900>
```

Printing the elements of a generator:

```python
def y_range(n:int):
    while n > 0:
        yield n
        n-=1

ten = y_range(10)

while True:
    try:
        print(next(ten))
    except StopIteration:
        break
```

Example:

Let's have an example where we want to create a generator that generates numbers from a range. We are going to call this generator `gen_numbers`

```py
def gen_numbers(start, stop, step):
    for n in range(start, stop, step):
        yield n

# generate multiples of 10 from 10 to 100
tens = gen_numbers(10, 100, 10)
print(next(tens)) # 10
print(next(tens)) # 20
# ... until you get an exception called 'StopIteration'
```

The good thing with generators is that they save memory. Even if we are generating a lot of numbers we still going to get the same size for the generator that has `10` elements and the one that has `10_000`

```py
import sys

tens_1 = gen_numbers(10, 100, 10)
tens_2 = gen_numbers(10, 100000, 10)
print(sys.getsizeof(tens_2))  # 232
print(sys.getsizeof(tens_1))  # 232
```

### Generator Expressions

```python
x = (i*i for i in range(5))
print(type(x), x)
```

Printing elements of a generator expression:

```python
x = (i*i for i in range(5))

while True:
    try:
        print(next(x))
    except StopIteration:
        break
```

> That's the basics about generators. [Ref](https://anandology.com/python-practice-book/functional-programming.html)

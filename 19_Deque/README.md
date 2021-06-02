### Generators
Generators simplifies creation of iterators. 
A generator is a function that produces a sequence of results instead of a single value.
> So a generator is also an iterator.

#### A simple generator
````python
def y_range(n:int):
    while n > 0:
        yield n
        n-=1

a = y_range(10)
print(a) # <generator object y_range at 0x0000022CDF411900>
````
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
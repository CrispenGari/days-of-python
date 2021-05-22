## Iterators 

There are many python objects that we can loop through using a ``for loop`` such as sets, lists, dictionaries, etc as follows:

```python
for ele in [1, 2, 7]:
    print(ele)
```
These are called **iterables**.

### The Iteration Protocol
The built-in function `iter` takes an iterable object and returns an iterator. Example:

```python
my_list = [i for i in range(6)]
list_iter = iter(my_list)
print(list_iter, type(list_iter)) # <list_iterator object at 0x000001FCB470F220> <class 'list_iterator'>
```

To access each element of an iterator we use the ``next`` method. Example let's print the elements of our `list_iter` we will do it as follows:

```python
my_list = [i for i in range(6)]
list_iter = iter(my_list)
for i in list_iter:
    print(i)
    
################ OR ###############
my_list = [i for i in range(6)]
list_iter = iter(my_list)
while True:
    try:
        print(next(list_iter))
    except StopIteration as e:
        print("The iteration runs out of elements")
        break

```
> Each time we call the ``next`` method on the iterator gives us the next element. If there are no more elements, it raises a ``StopIteration``.

Iterators are implemented as classes. Here is an iterator that works like built-in `range` function.

````python
class xrange:
    def __init__(self, start, stop, step=1):
        self.start = start - step
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration()
        else:
            self.start += self.step
        return self.start


my_range = xrange(0, 10, 2)

while True:
    try:
        print(next(my_range))
    except StopIteration as e:
        print("The iteration runs out of elements")
        break
````
> That's the basics about generators. [Ref](https://anandology.com/python-practice-book/iterators.html)












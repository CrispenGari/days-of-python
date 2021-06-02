### Deque
A double ended que. Which allows us to add or remove items from both ends.
* This is also coming from collections



#### A simple deque
````python
from collections import deque
my_deque = deque([1, 2, 3])
print(my_deque)
````
Adding elements to a deque in both ends

```python
from collections import deque
my_deque = deque([1, 2, 3])
my_deque.append(4) # adding elements to the right
my_deque.appendleft(-2) # adding elements to the left
print(my_deque)
```
There are a lot of methods that are in the ``deque`` collections, which can be found in the official docs.

> Python Docs. [Ref](https://docs.python.org/3/library/collections.html)
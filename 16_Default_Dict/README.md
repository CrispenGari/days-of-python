### Default Dict
Returns a new dictionary-like object. defaultdict is a subclass of the built-in dict class. It overrides one method and adds one writable instance variable.
* This dictionary is different from the ``dict`` in the sense that if we try to access elements that doesn't exist in a `dict` it raises an error but in this one it doesn't throw an error, instead it returns a default value. Let's see this in action. 
* This default dict is comming from ``collections``

#### A simple DefaultDict
````python
from collections import defaultdict

default_dict = defaultdict(list, {
    "name": "Hello",
    "age" : 21,
    "yob": 2001
})
print(default_dict)
````
Printing the elements of a defaultdict:
```python
from collections import defaultdict

default_dict = defaultdict(int, {
    "name": "Hello",
    "age" : 21,
    "yob": 2001
})
print(f"Name: {default_dict['name']}, Age: {default_dict['age']}, YOB: {default_dict['yob']}, Gender: {default_dict['gender']}")
```
If the key of an element does not exist it will return ``0`` this is because we have set default as ``int``. We can set it to an `float`, a ``list`` or whatever we want.

> Python Docs. [Ref](https://docs.python.org/3/library/collections.html)
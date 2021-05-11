## Counter Class Python Collections

* This function helps us to count the occorance of each instance in a collection.
* This function returns a Dictionary mapped iterm to the number of occurance of the item.

  
<p align="center">
  <img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
 <img src="https://img.shields.io/static/v1?label=package&message=random&color=red"/>
 <img src="https://img.shields.io/static/v1?label=package&message=collections&color=orange"/>
</p>

### Examples
````python
from collections import Counter
from random import randrange
numbers = [randrange(0, 4) for i in range(20)]

numbers_dict = Counter(numbers)
print(numbers_dict)
````
### The counter object
This allows us to create a counter instance. Let's say we want to count the number of ocurance 
of certain objects in a list. The alternative apart from the previous example is 
by creating a counter object and then append counts in a loop.

````python
from collections import Counter
from random import randrange
numbers = [randrange(0, 4) for i in range(20)]
counter = Counter()
for number in numbers:
    counter[number] += 1

print(counter)
````

Let's say we know the elements in a list, and we want to perform the count of the ocurance of each 
element in a list we can do it as follows using a python dictionary.

````python
numbers = [1, 1, 2, 3, 1, 1, 2, 2, 3, 2, 1, 1]

counter = {1:0, 2:0, 3: 0}
for number in numbers:
    counter[number] += 1
print(counter)
````

### So why the ``Counter``?
The counter come up with the helper functions, such as the ``most_commen(n)`` which returns
the most common elements in a list.

````python
from collections import Counter
from random import randrange

numbers = [randrange(0, 4) for i in range(20)]

counter = Counter()
for number in numbers:
    counter[number] += 1

print(counter.most_common(2))
````

> That's it about the filter function.
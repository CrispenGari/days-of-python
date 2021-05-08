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

> That's it about the filter function.
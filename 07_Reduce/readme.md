## Reduce Function Python
`reduce` function performs operations and return a result on collection. Reduce takes 3 parameters which are
* **the function** - what operation are you applying on the collection
* **collection** - a list, set, etc of iterabables
* **initializer?** - start-value and it is optional

<p align="center">
  <img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
 <img src="https://img.shields.io/static/v1?label=packege&message=functtools&color=red"/>
</p>

### Examples
1. Getting the sum in a list

```python 
from functools import reduce
numbers = [i for i in range(10)]
def add(x, y):
    return x+y
sum = reduce(add, numbers,0 )
print(sum)            ## 45                                 
```

2. reduce on a list of dictioneries:
```python
from functools import reduce

numbers = [
    {"number": 1},
    {"number": 2},
    {"number": 3},
    {"number": 4},
    {"number": 5},
]

def add(x, y):
    return x + y["number"]

sum = reduce(add, numbers, 0)
print(sum)    ##   15                             
```

3. becoming more fancy in a dict map using reduce + OOP
````python

from functools import reduce

class Number:
    def __init__(self, number):
        self.number = number

numbers = [
    {"number": 1},
    {"number": 2},
    {"number": 3},
    {"number": 4},
    {"number": 5},
]

def add(x, y):
    return x + y.number
sum = reduce(add, [Number(number["number"]) for number in numbers], 0)
print(sum)
````

> That's the basics about the ``reduce`` function
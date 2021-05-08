## Enum -- Python
Enum is a class in python for creating enumerations, which are a set of symbolic names (members) bound to unique, constant values

<p align="center">
  <img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
 <img src="https://img.shields.io/static/v1?label=packege&message=enum&color=red"/>
</p>

### Installation
```shell
pip install enum34
```

### Examples

## Basic Creation and Inheritance of class Colors from the Enum class

````python
from enum import Enum
class Colors(Enum):
    red = 1
    blue = 2
    green = 3
print(Colors.red) ## Colors.red
print([c for c in Colors]) ## [<Colors.red: 1>, <Colors.blue: 2>, <Colors.green: 3>]
````
### Accessing elements of the Enum
```python
from enum import Enum

class Colors(Enum):
    red = 1
    blue = 2
    green = 3
print([c.name for c in Colors]) ## ['red', 'blue', 'green']
```

> That's the basics of ``enums`` in python
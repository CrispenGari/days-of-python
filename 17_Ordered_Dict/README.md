### OrderedDict
Return an instance of a dict subclass that has methods specialized for rearranging dictionary order.
* Elements are arranged in the way they are added.
* This is coming from the collection package
#### A simple OrderedDict
````python
from collections import OrderedDict

my_dict = OrderedDict()
my_dict["name"] = "Name"
my_dict["age"] = 54
my_dict["sex"] = "Male"
print(my_dict) ## OrderedDict([('name', 'Name'), ('age', 54), ('sex', 'Male')])
````
Printing the elements of an OrderedDict():
```python
from collections import OrderedDict
my_dict = OrderedDict()
for i in range(10):
    my_dict[i] = i**2

for i in range(10):
    print(my_dict[i])
```
Maybe there's a special case where one would need to apply this because the  python `dict` already have the functionality
an OrderedDict has.
> Python Docs. [Ref](https://docs.python.org/3/library/collections.html)
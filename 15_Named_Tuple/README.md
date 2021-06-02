### ``namedtuples`` 
Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code.
* They behave the same as ``struct`` in c++.
* They come from collections

#### A simple ``namedtuple``
````python
from collections import namedtuple
Student = namedtuple(
    "Student",
    ["name", "age", "module"]
)
student = Student("Mark", 21, "IT")
print(student)
````

Printing the elements of a namedtuple:
```python
from collections import namedtuple
Student = namedtuple(
    "Student",
    ["name", "age", "module"]
)
names = ["Name1", "Name2", "Name3", "Name4"]
students = []
for name in names:
    students.append(Student(name, 21, "IT"))
for student in students:
    print(f"Name: {student.name}, Age: {student.age}, Module: {student.module}")
```
### Creating nested namedtuples

```python
from collections import namedtuple
Module = namedtuple("Module",
                    ["name", "code"]
                    )
Student = namedtuple(
    "Student",
    ["name", "age", "module"]
)
student = Student("Hello", 23, Module("IT", 224))

```
Printing elements of a nested namedtuple:

```python
from collections import namedtuple
Module = namedtuple("Module",
                    ["name", "code"]
                    )
Student = namedtuple(
    "Student",
    ["name", "age", "module"]
)
names = ["Name1", "Name2", "Name3", "Name4"]
modules = ["IT", "DS", "AI", "ML"]
students = []
for name, module in zip(names, modules):
    students.append(Student(name, 21, Module(module, 221)))
for student in students:
    print(f"Name: {student.name}, Age: {student.age}, Module Name: {student.module.name}, Module Code: {student.module.code}")
```

> Python Docs [Ref](https://docs.python.org/3/library/collections.html)
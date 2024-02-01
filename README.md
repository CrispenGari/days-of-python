### Days of python

This repository contains some cool python code examples and explanations that you can learn some cool features beginner to expect with the python language.

> **Hello Word!!**

```py
class Vector:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, z=self.z + other.z)

    def __repr__(self) -> str:
        return "{cn}<x={x}, y={y}, z={z}>".format(
            x=self.x, y=self.y, z=self.z, cn=self.__class__.__name__
        )


v1 = Vector(2, 3, 4)
v2 = Vector(5, 6, 7)
res = v1 + v2
print(res)
```

<p align="center">
  <img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
</p>

### Argument and Keyword Augments

Let's talk about how the argument and keyword arguments works and how to use them. Let's say we don't know what arguments are going to be passed to a function `hi` defining a function signature as `def hi(*args, **kwargs):` helps us to get the arguments and keyword args that were passed to the function `hi`

```py
def hi(*args, **kwargs):
    """
    args: will be a tuple of arguments passed to a function
    kwargs: a dictionary of key word arguments passed to the function
    """
    return args, kwargs

args, kwargs = hi("Jonh", 10, name="Jonh", age=10)
print(args)
print(kwargs)
```

Result:

```shell
('Jonh', 10)
{'name': 'Jonh', 'age': 10}
```

### Argument Parsing

In python we can get the arguments from the terminal when running python script using the `sys` module. Let's have a look at how we can get the arguments parsed when running a python script called `main.py`

```py
import sys
args = sys.argv
print(args)
```

Running the command

```shell
python main.py name hello there
```

Will result in the following arguments being retrieved. `['main.py', 'name', 'hello', 'there']`

> Note that the first argument will be the script name that you run and anything after that in the list will be strings that you parsed after the file name. All the arguments that you parse here will be returned as strings separated by a space. If you want to escape a space you will need to use quotes `""`:

```shell
python main.py message "hello there"
```

> Result will be: `['main.py', 'message', 'hello there']`

What if we want to use some optional arguments. We can do it as follows

```py
import sys
import getopt
# python main.py -p 3001 -h 127.0.0.1 -o https
opts, args = getopt.getopt(sys.argv[1:], "p:h:o:", ["port=", "host=", "protocol="])
print(opts, args)
```

Now if we run

```shell
python main.py -p 3001 -h 127.0.0.1 -o https
```

We will get the following optional arguments and args that were parsed when running the script

```shell
[('-p', '3001'), ('-h', '127.0.0.1'), ('-p', 'https')] []
```

Note that you can also type required arguments in the script and run the command using `long` options names but for that you will need to use the `--` instead of a single `-`.

```py
import sys
import getopt

# python main.py --port 3001 --host 127.0.0.1 --protocol wss message "hello world"
opts, args = getopt.getopt(sys.argv[1:], "p:h:pt:", ["port=", "host=", "protocol="])

print(dict(opts), args)
```

Running the command:

```shell
python main.py --port 3001 --host 127.0.0.1 --protocol wss message "hello world"
```

You will get the following result:
shell

```shell
{'--port': '3001', '--host': '127.0.0.1', '--protocol': 'wss'} ['message', 'hello world']
```

### Factory Design Patten

In python we can create interfaces for classes and implement them. For that we need to use the `abc` package that is built in in python. Let's create an `IUser` interface that will contain a class method called `hi`

```py
from abc import abstractmethod, ABCMeta

class IUser(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def hi(self, name: str) -> str:
        """This is hi menthod"""


IUser().hi("Bob")
```

If you try to do that you will get an error saying

```
TypeError: Can't instantiate abstract class IUser without an implementation for abstract method 'hi'
```

So let's use this interface to create a class called `Student` that will inhherit from `IUser`

```py
class Student(IUser):
    pass
Student().hi("Bob")
```

If i try to do this i will get an error telling me that i haven't implemented `hi`

```
TypeError: Can't instantiate abstract class Student without an implementation for abstract method 'hi'
```

To solve this error we are going to change our code to:

```py
class Student(IUser):
    def __init__(self) -> None:
        super().__init__()

    def hi(self, name):
        print("Hello {name}".format(name=name))

Student().hi("Bob")
```

Note that we can also define some property `staticmethod` and also `property` here is san example:

```py
from abc import abstractmethod, ABCMeta

class IUser(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def hi(self, name: str) -> str:
        """This is hi menthod"""

    @staticmethod
    @abstractmethod
    def programmer(name):
        """"""

    @property
    @abstractmethod
    def Name(self):
        """Name of the user"""


class Student(IUser):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.__name = name
    def hi(self, name):
        print("Hello {name}".format(name=name))

    @property
    def Name(self):
        return self.__name

    @staticmethod
    def programmer(name):
        return name

stud = Student(name="Julie")
stud.hi("Bob")
print(stud.Name)
print(stud.programmer("Namo"))

```

We can create different classes that inherits from our `interface` and then create a Factory class `UserFactory` that helps us to return a factory object of different objects based on the type passed.

```py
from abc import abstractmethod, ABCMeta

class IUser(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def hi(self, name: str) -> str:
        """This is hi menthod"""
class Student(IUser):
    def hi(self, name):
        print("Student {name}".format(name=name))
class Manager(IUser):
    def hi(self, name):
        print("Manager {name}".format(name=name))
class Other(IUser):
    def hi(self, name):
        print("Other {name}".format(name=name))

class UserFactory:
    @staticmethod
    def get_user(type: str):
        if type.lower() == "student":
            return Student()
        if type.lower() == "manager":
            return Manager()
        return Other()

UserFactory.get_user("student").hi("Bob")
UserFactory.get_user("manager").hi("Bob")
UserFactory.get_user("haha").hi("Bob")

```

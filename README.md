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

### Proxy Design Patten

This design pattern allows us to wrap functionality among other classes in python.

Let's say we have a class called person and this class has a static method to be implemented from `IUser` called `hi`. We can create a `ProxyUser` class and also make it to inherit from `IUser`

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

class ProxyUser(IUser):
    def __init__(self) -> None:
        super().__init__()
        self.student = Student()
    def hi(self, name: str):
        self.student.hi(name)
        print(f"Hi I am a proxy class: {name}")

ProxyUser().hi("Bob")
```

With this flexibility we can call the `student` object in the `Proxy` class when we call the method `hi` on `ProxyUser` we also trigger the `hi` method in the student class.

### Singleton Design Pattern

The idea behind this is that we only have 1 class and this class will only have `1` instance. So let's go ahead and implement thats.

```py
from abc import abstractmethod, ABCMeta

class ISession(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_session():
        """To be implemented"""

class Session:
    __instance = None
    @staticmethod
    def get_instance():
        if Session.__instance is None:
            Session("localhost", 5432)
        return Session.__instance
    def __init__(self, host: str, port: int) -> None:
        if Session.__instance is not None:
            pass
            # raise Exception(f"{self.__class__.__name__} can only be initialized once.")
        else:
            self.host = host
            self.port = port
            Session.__instance = self
    @staticmethod
    def get_session():
        return {"port": Session.__instance.port, "host": Session.__instance.host}
```

Now we can create a single instance of a `Session` class because of this logic. If we try to check the instance of `session` and `session1` they will be located in the same memory:

```py
session1 = Session("localhost", 5432)
print(session1.get_session())
print(session1.get_instance())
session = Session("localhost", 5432)
print(session.get_session())
print(session.get_instance())
```

Output:

```shell
{'port': 5432, 'host': 'localhost'}
<__main__.Session object at 0x0000018C15D39FA0>
{'port': 5432, 'host': 'localhost'}
<__main__.Session object at 0x0000018C15D39FA0>
```

### Composite Design Patten

Let's say we have `IDepartment` which is the base interface for our departments `Testing` and `Deploying`. Each department has a method of printing the department employees. Then the base department class `Development` can print all the information about other departments including it's information. This is how it can be done.

```py
from abc import abstractmethod, ABCMeta

class IDepartment(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, employees):
        """To be implemented"""
    @staticmethod
    @abstractmethod
    def print_department():
        """"""

class Testing(IDepartment):
    def __init__(self, employees):
        self.employees = employees
    def print_department(self):
        print(f"Testing: {self.employees}")

class Deploying(IDepartment):
    def __init__(self, employees):
        self.employees = employees
    def print_department(self):
        print(f"Development: {self.employees}")

class Development(IDepartment):
    def __init__(self, employees):
        self.employees = employees
        self.deps = list()
        self.all_employees = employees
    def add_department(self, dep):
        self.deps.append(dep)
        self.all_employees += dep.employees

    def print_department(self):
        print(f"Department Employees: {self.all_employees}")
        for dep in self.deps:
            dep.print_department()
        print(f"Total Employees: {self.employees}")

```

```py

```

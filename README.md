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

### Data Classes

These are a cool python feature that we can use on our python class so that we won't define some `__method__` as they will be defined for us once we decorate the class with the `dataclass` decorator that comes from `dataclasses`. Let's consider the following example where we have a class called `Person`

```py
from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: str
    gender: str
person = Person("bob", 5, 7)
print(person) # Person(name='bob', age=5, gender=7)
```

When defining the person class we might want to make the `person` object immutable for that we can specify the argument when decorating our class called `frozen`:

```py

@dataclass(frozen=True)
class Person:
    name: str
    age: str
    gender: str
person = Person("bob", 5, 7)
person.age = 18 # this will throw an error
print(person)
```

We can also specify our dataclass `Person` that it only takes in `keyword` arguments by passing the following options.

```py
@dataclass(frozen=True, kw_only=True)
class Person:
    name: str
    age: str
    gender: str
person = Person(name="bob", age=5, gender="M") # only kwargs will be allowed
```

The good thing with dataclasses is that you can overide the default `__method__` that are in the dataclass for example let's overide the `__repr__()` method we can do it as follows:

```py
@dataclass(frozen=True, kw_only=True)
class Person:
    name: str
    age: str
    gender: str
    def __repr__(self) -> str:
        return "Person {}".format(self.name)
person = Person(name="bob", age=5, gender="M")
print(person) # Person bob
```

We can also set default values to dataclases let's have a look at the following example

```py
from dataclasses import dataclass, field
import random
import string

def uuid():
    return "".join(random.choices(string.ascii_lowercase, k=5))

@dataclass(frozen=False, kw_only=True, slots=True)
class Person:
    name: str
    age: str
    gender: str
    id: str = field(default_factory=uuid, init=False)
    online: bool = True
    colors: list[str] = field(
        default_factory=list,
    )
    _search_str: str = field(init=False, repr=False)
    def __post_init__(self):
        self._search_str = f"{self.name}%20{self.age}"
person = Person(name="bob", age=5, gender="M")
print(person)

```

Now we have introduced another function called `field`. It takes in some number of arguments, for the default value of `id` we want to generate it using a function called `uuid` and for that we need to pass in an argument called `default_factory`, if we don't want to see a property in the `dander` method we can set `repr` to False. We have a `dander` method `__post_init__` which allows us to post initilize the `_search_str` when we create an instance of a `Person`. You can pass a lot of arguments in this `field` method.

### Generics in Python `3.12`

In this section we are going to have a look at how we can work with generics in `python`. Let's say we have a function that returns a first element in an array and we want to make this function generic. This is how we can achieve that befor and after python `3.12`

Before:

```py
from typing import TypeVar

T = TypeVar('T')

def get_first(ele:list[T])-> T:
    return ele[0]
strs = ['hi', 'hey']
ints = [2, 4]

val = get_first(strs) # str
val = get_first(ints) # int

```

After:

```py
def get_first[T](ele: list[T]) -> T:
    return ele[0]

strs = ["hi", "hey"]
ints = [2, 4]

val = get_first(strs)  # str
val = get_first(ints)  # int

```

Let's have a look at an example where we can use generics in python classes

Before:

```py
from typing import  TypeVar, Generic
from dataclasses import dataclass

T = TypeVar("T")
class Car(Generic[T]):
    def __init__(self, car: T) -> None:
        self.car = car
    def set_car(self, car: T) -> None:
        self.car = car
    def get_car(self) -> T:
        return self.car
@dataclass(kw_only=True)
class Vehicle:
    name: str
    license_plate: str

car = Car(Vehicle(name="Audi", license_plate="DGB 56"))
my_car = car.get_car() # type Vehicle

```

After:

```py
from dataclasses import dataclass
class Car[T]:
    def __init__(self, car: T) -> None:
        self.car = car
    def set_car(self, car: T) -> None:
        self.car = car
    def get_car(self) -> T:
        return self.car
@dataclass(kw_only=True)
class Vehicle:
    name: str
    license_plate: str

car = Car(Vehicle(name="Audi", license_plate="DGB 56"))
my_car = car.get_car() # type Vehicle
```

We can restrict the type of a generic by using `bound` let's consider an example where we have a class `Plane`, `Car` and a `Boat` and all these classes are inheriting from a dataclass `Vehicle`.

```py
from typing import TypeVar, Generic
from dataclasses import dataclass

@dataclass(kw_only=True)
class Vehicle:
    name: str
    def display(self) -> None:
        print(f"Vehicle Name: {self.name}")

class Boat(Vehicle):
    def display(self) -> None:
        print(f"Boat Name: {self.name}")
class Plane(Vehicle):
    def display(self) -> None:
        print(f"Plane Name: {self.name}")
class Car(Vehicle):
    def display(self) -> None:
        print(f"Car Name: {self.name}")
```

We want to create a registry class that will set bound on a certain type of a vehicle. We can do it as follows:

Before:

```py
V = TypeVar("V", bound=Vehicle)
class Registry(Generic[V]):
    def __init__(self) -> None:
        self.vehicles: list[V] = []

    def add(self, v: V) -> None:
        self.vehicles.append(v)

    def display_all(self) -> None:
        for v in self.vehicles:
            v.display()

registry = Registry[Car]()
registry.add(Car(name="Jeep"))
registry.add(Car(name="Toyota"))
registry.add(Plane(name="Jet"))  # this is a type error
registry.display_all()
```

If we want our `registry` to accept all the vehicle types and the or it subclass we can then do it as follows:

```py
registry = Registry[Vehicle]()
registry.add(Car(name="Jeep"))
registry.add(Boat(name="Yacht"))
registry.add(Plane(name="Jet"))
registry.display_all()
```

That was before now after python `3.12` we can do it as follows:

```py

class Registry[T: Vehicle]:
    def __init__(self) -> None:
        self.vehicles: list[T] = []
    def add(self, v: T) -> None:
        self.vehicles.append(v)
    def display_all(self) -> None:
        for v in self.vehicles:
            v.display()

registry = Registry[Car]()
registry.add(Car(name="Jeep"))
registry.add(Car(name="Toyota"))
registry.add(Plane(name="Jet"))  # this is a type error
registry.display_all()

```

If we want our `registry` to accept all the vehicle types and the or it subclass we can then do it as follows:

```py
registry = Registry[Vehicle]()
registry.add(Car(name="Jeep"))
registry.add(Boat(name="Yacht"))
registry.add(Plane(name="Jet"))
registry.display_all()
```

We can also constrain our `Registry` class so that it can take a `Car` or a `Boat` as follows:

```py

class Registry[T: (Car, Boat)]:
    def __init__(self) -> None:
        self.vehicles: list[T] = []

    def add(self, v: T) -> None:
        self.vehicles.append(v)

    def display_all(self) -> None:
        for v in self.vehicles:
            v.display()

registry = Registry[Car]()
registry.add(Car(name="Jeep"))
registry.add(Boat(name="Yacht"))
registry.display_all()
```

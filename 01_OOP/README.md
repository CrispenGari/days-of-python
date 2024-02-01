## OOP - Object Oriented Programing - Python

### Classes and Objects

<p align="center">
  <img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
</p>

### Class:

A class is a blueprint that defines the variables and the methods (Characteristics) common to all objects of a certain kind.

### Object:

An object is an entity that has a state and behavior associated with it.
Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects.
More specifically, any single integer or any single string is an object. The number 12 is an object, the string “Hello, world” is an object,
a list is an object that can hold other objects, and so on.

### The `__init__` method

The `__init__`method is similar to constructors in C++ and Java.
It is run as soon as an object of a class is instantiated.
The method is useful to do any initialization you want to do with your object.

### The self

Class methods must have an extra first parameter in the method definition.
We do not give a value for this parameter when we call the method, Python provides it
If we have a method that takes no arguments, then we still have to have one argument – the self.

### Class and Instance Variables (Or attributes)

- In Python, **instance variables** are variables whose value is assigned inside a **constructor** or method with self.
- Class variables are variables whose value is assigned in class.

### Coding!!

### Basic class Creation.

This is how you can define a class in python.

```python
class Dog():
    pass
```

### The `__init__(self)`

- This runs as soon as the object of a class is created

```python
class Dog():
    def __init__(self):
        print("I am a dog")
Dog() ## I am a dog
```

### The `__del__(self)`

This method runs when an object is being deleted, it is called a `destructor` here is an example showing how it works:

```py
class Person:
    def __init__(self) -> None:
        print("The constructor has been called")

    def __del__(self):
        print("The destructor has been called")
```

### Class Variables vrs Instance variables

Remember instance variables are variables that are declared inside the `__init__(self)` method with
`self.variable` while class variables are just variables that belongs to the whole class.

```python
class Dog:
    name = "Broke" # class variables
    def __init__(self, age):
        self.age = age # instance variable

    def __call__(self, *args, **kwargs):
        print("my name is {} and i am {} years old.".format(self.name, self.age))
dog = Dog(15)
dog()
```

### The `__call__(self, *args, **kwargs)`

This is a special method that will be called as soon as the object is called as a function for example when we call the object of type `Dog` as `dog()` the `__call__` method runs.

### The `__len__(self)`

```python
class Dog:
    numbers = [i for i in range(10)]
    def __init__(self):
        self.count = len(self.numbers)

    def __len__(self):
        return self.count
dog = Dog()
print(len(dog))
```

The `__len__(self)__` method runs when we try to find the `len` of an object using the `len()` function.

### The `__getitems__`

This method runs when we try to index an object.

```python
class Dog:
    numbers = [i for i in range(10)]
    def __init__(self):
        self.count = len(self.numbers)

    def __getitem__(self, item):
        return self.numbers[item]

dog = Dog()
print(dog[1])
```

### The `__str__`

This method get called when we try to print an object of a class instance.

```python
class Dog:
    numbers = [i for i in range(10)]
    def __init__(self):
        self.count = len(self.numbers)

    def __str__(self):
        return "I want to print"
dog = Dog()
print(dog)
```

### The `__add__(self, other)`

This method runs when we try to add a number to an object of type class.

```python
class Dog:
    numbers = [i for i in range(10)]
    def __init__(self):
        self.count = len(self.numbers)

    def __add__(self, other):
        return self.count + other
dog = Dog()
print(dog + 10)
```

Here is another example of adding objects on class `Vector`

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

### The `__sub__(self, other)`

This method runs when we try to subtract an object with a number

```python
class Dog:
    numbers = [i for i in range(10)]
    def __init__(self):
        self.count = len(self.numbers)

    def __sub__(self, other):
        return self.count - other
dog = Dog()
print(dog - 10)
```

### The `__div__(self, other)`

This method runs when we try to divide an object with a number

```python
class Dog:
    numbers = [i for i in range(10)]
    def __init__(self):
        self.count = len(self.numbers)

    def __div__(self, other):
        return self.count - other
dog = Dog()
print(dog.__div__(10))
```

### The `__divmod__(self, other)`

This method runs when we try to find the `divmod` of an object.

```python
class Dog:
    numbers = [i for i in range(10)]
    def __init__(self):
        self.count = len(self.numbers)

    def __divmod__(self, other):
        return self.count - other
dog = Dog()
print(dog.__divmod__(10))
```

### The `__mult__(self, other)`

This method runs an operation under it when ever we try to multiply an object with a number

```python
class Dog:
    numbers = [i for i in range(10)]
    def __init__(self):
        self.count = len(self.numbers)

    def __mul__(self, other):
        return self.count - other
dog = Dog()
print(dog * 10)
```

### Data Hiding in OOP

In Python, we use double underscore (Or \_\_) before the attributes
to declare a `private` variable and a single underscore for protected variables.

```python
class Dog:
    numbers = [i for i in range(10)]
    def __init__(self):
        self.count = len(self.numbers)
        self._weight = 45
        self.__surname = "Martinez"
dog = Dog()
print(dog.__surname) ## Dog has no attribute surname
print(dog._weight) ## 45
```

#### Accessing Private variables

To access them we can use setters and getters, for example:

```python
class Dog:
    numbers = [i for i in range(10)]
    def __init__(self):
        self.count = len(self.numbers)
        self._weight = 45
        self.__surname = "Martinez"
    def setSurname(self, new):
        self.__surname = new

    def getSurname(self):
        return self.__surname
dog = Dog()
print(dog.getSurname()) ## "Martinez"
dog.setSurname("New")
print(dog.getSurname()) ## "New"
print(dog._weight) ## 45
```

Another way also create a property called `Surname` and annotate it with `@property` and do method overloading and annotate another `Surname` class with `@Surname.setter`.

```py
class Dog:
    def __init__(self, surname, weight):
        self._weight = weight
        self.__surname = surname
    @property
    def Surname(self):
        return self.__surname
    @Surname.setter
    def Surname(self, value):
        self.__surname = value
dog = Dog("Jack", 56)
dog.Surname = "Mewww"
print(dog.Surname)
```

Now with that we can modify our properties directly and get them using the `.Surname`.

### Inheritance

One of the major advantages of Object Oriented Programming is re-use. Inheritance is one of the mechanisms to achieve the same. In inheritance, a class (usually called superclass) is inherited by another class (usually called subclass). The subclass adds some attributes to superclass.
Inheritance allows us to define a class that inherits all the methods and properties from another class.

- **Parent class** - is the class being inherited from, also called base class.
- **Child class is** - the class that inherits from another class, also called derived class.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def printName(self):
        print("I am a {}".format(self.name))
class Cat(Animal):
    pass
class Dog(Animal):
    pass
cat = Cat("Cat")
dog = Dog("Dog")
cat.printName()
dog.printName()
```

> **You can also do it as follows**

```python

class Animal:
    def __init__(self, name):
        self.name = name
    def printName(self):
        print("I am a {}".format(self.name))
class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

cat = Cat("Cat")
dog = Dog("Dog")
cat.printName()
dog.printName()
```

### The `super()` Function

Python also has a super() function that will make the child class inherit all the methods and properties from its parent.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def printName(self):
        print("I am a {}".format(self.name))
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

cat = Cat("Cat")
dog = Dog("Dog")
cat.printName()
dog.printName()
```

### Class method vs Static methods

#### Class Methods

The `@classmethod` decorator, is a builtin function decorator that is an expression that gets evaluated after your function is defined. The result of that evaluation shadows your function definition.

- A class method receives the class as implicit first argument, just like an instance method receives the instance.
- A class method is a method which is bound to the class and not the object of the class.
- They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
- It can modify a class state that would apply across all the instances of the class. For example it can modify a class variable that will be applicable to all the instances.

#### Static Methods

- A static method does not receive an implicit first argument `self`.
- A static method is also a method which is bound to the class and not the object of the class.
- A static method can't access or modify class state.
- It is present in a class because it makes sense for the method to be present in class.

```python

class Dog:
    def __init__(self):
        pass
    @staticmethod
    def greater(a):
        return a > 6
    @classmethod
    def printHello(cls, name):
        print("Hello " + name)

dog = Dog()
print(dog.greater(5))
dog.printHello("hi")
```

> Note: You can define a static method without annotating it using the `@staticmethod` and you can call it directly without initializing an object direct from the class for example:

```py
Dog.printHello("Dog")
print(Dog.greater(45))
```

That's the basics about classes and objects.

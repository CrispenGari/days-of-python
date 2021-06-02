### Decorators
A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it

#### A simple decorator

````python
def simple_decorator(fn):
    def wrapper():
        print("Start")
        fn()
        print("End")
    return wrapper()
def say_hello():
    print("Hello there human")
simple_decorator(say_hello)
````
* We created a function that accept a function as it's argument.
* Then as python function can have functions inside them a decorator has an inner function which will be returned
by the decorator function.
  
* When we call ``simple_decorator`` and pass `say_hello` in it the following will be the output.
````shell
Start
Hello there human
End
````
* Similarily the above can be done as follows:
````python
def simple_decorator(fn):
    def wrapper():
        print("Start")
        fn()
        print("End")
    return wrapper()

@simple_decorator
def say_hello():
    print("Hello there human")
````
We have called the ``@simple_decorator`` which will take `say_hello` as it's argument and do the same thing as we did previously. 
The second way is the most commonly used way when dealing with function decorators.

### Reusing decorators
Decorators can be reused, for example take a look at the following example, where we will print "hello there human" twice.
```python
def simple_decorator(fn):
    def wrapper():
        fn()
        fn()
    return wrapper()
@simple_decorator
def say_hello():
    print("Hello there human")
```
### Decorating Functions With Arguments
It's not always the case that we decorate the function that doesn't take arguments. Let's consider the following case where our function `say_hello` takes an argument name and print out the name:

```python
def simple_decorator(fn):
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)
    return wrapper

@simple_decorator
def say_hello(name):
    print(f"Hello there {name}")
say_hello("Crispen")

```

### A decorator that returns a value.

To return values from a decorator function we have to be sure that our function that is decorated returns a value. In this case the `wrapper()` function should return the function. 
It's difficult to explain let's write some code to implement a decorator that returns a value.

```python
def simple_decorator(fn):
    def wrapper(*args, **kwargs):
        res = fn(*args, **kwargs)
        return res
    return wrapper
@simple_decorator
def say_hello(name):
    return name.upper()
print(say_hello("Crispen"))
```
In this example we created a decorator `simple_decorator` which takes a function in it in this case 
`say_hello` and `say_hello` accept name as it's parameter and return name converted to uppercase.
* Then the wrapper function in the decorator will then returns another the result of the function that was accepted by the decorator.

### Getting the names of decorators.
In python if we call:
```python
print(print.__name__) 
```
We get `"print"` which is the name of the print function. We also want to say if we call:
```python
print(say_hello.__name__)
```
We want to get ``say_hello``. Let's try that.
```python
def simple_decorator(fn):
    def wrapper(*args, **kwargs):
        res = fn(*args, **kwargs)
        return res
    return wrapper
@simple_decorator
def say_hello(name):
    return name.upper()
print(say_hello.__name__)
```
 The  output is `wrapper` wow. So how do we get `say_hello`?. This is easy, we can use `functtool` decorator `wrapper` to do that let's se what we will get.


````python
import functools
def simple_decorator(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        res = fn(*args, **kwargs)
        return res
    return wrapper
@simple_decorator
def say_hello(name):
    return name.upper()
print(say_hello.__name__)
````
All we did was to call ``@functools.wraps(fn)`` in our decorator. The output will be `say_hello`

### A real world example.
Let's say we have a function that prints the clock tick every second. By using decorators we can make our life very easy consider the following code:

```python
import functools, time
def second_decorator(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        time.sleep(1)
        res = fn(*args, **kwargs)

        return res
    return wrapper

@second_decorator
def timer(i):
    return i
for i in range(10):
    print(timer(i))
```
### Decorators With Arguments
Sometimes, it’s useful to pass arguments to your decorators. Let's take a look at the following example:

````python
import functools
def repeat(n):
    def simple_decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                res = fn(*args, **kwargs)
            return res
        return wrapper
    return simple_decorator
@repeat(5)
def say_hello(name):
    print("Hello " + name)
say_hello("World")
````
* [Good Explanation](https://realpython.com/primer-on-python-decorators/)

### Classes as Decorators
The following snippet shows how we can create class decorators.
```python
import functools
class ClassDecorator:
    def __init__(self, func):
        functools.wraps(self, func)
        self.func = func
        self.n_count = 0
    def __call__(self, *args, **kwargs):
        self.n_count += 1
        print(f"You have called {self.func.__name__} {self.n_count} time(s).")
        return self.func(*args, **kwargs)
@ClassDecorator
def hello():
    print("Hello World")
hello()
hello()
```
> More details and good explanation. [Ref](https://realpython.com/primer-on-python-decorators/)
## Lambda functions -- Python
A Lambda Function in Python programming is an anonymous function or a function having no name. 
It is a small and restricted function having no more than one line. Just like a normal function, a 
Lambda function can have multiple arguments with one expression

<p align="center">
  <img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
 <img src="https://img.shields.io/static/v1?label=packege&message=functtools&color=red"/>
</p>

### Examples

1. Creating a lambda function that adds 2 numbers
````python
add = lambda x, y: x+y
print(add(10, 6))
````

2. Creating a lambda function that convert a string to uppercase
````python
upper = lambda x:x.upper()
print(upper("dog"))
````

3. Creating a lambda function that prints something
```python
print_name = lambda x:print("Your name is: ", x)
print(print_name("dog"))
```

4. Immediately call the lambda function.
````python
(lambda x:print("Your name is: ", x))("dog")
````

5. lambda in reduce function
````python
from functools import reduce
sum = reduce(lambda x, y: x+y, [i for i in range(5)], 0)
print(sum) ## 10
````

6. lambda in map function
````python
list_ = map(lambda x: x**2, [i for i in range(5)])
print(list(list_)) ## [0, 1, 4, 9, 16]
````

7. filter in reduce function
````python
list_ = filter(lambda x: x>=3, [i for i in range(5)])
print(list(list_)) ## [3, 4]

````
8. lists comprehension
````python
list_ = [(lambda x:x**3)(x) for x in range(10)]
print(list(list_))
````

> That's the basics about the ``lambda`` functions.
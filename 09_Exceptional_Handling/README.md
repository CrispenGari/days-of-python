## Exceptional Handling in Python
This is the way of handling errors in python.

<p align="center">
  <img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
</p>

### Examples:
```python
try:
    print(18./0)
except Exception as e:
    print("You cant divide by 0:", e)
finally:
    pass

```
### Creating a Custom Exception
To create a custom exception we need to create a class that Inherit from the `Exeption` class example:
```python
class SmallSizeException(Exception):
    pass

def printList(list_):
    try:
        if len(list_) < 10:
            raise SmallSizeException("The list size is too small")
        else:
            print(list_)
    except SmallSizeException as e:
        print(e)
    finally:
        pass

printList([i for i in range(5)])
```
> That's how we can create and handle errors in python.
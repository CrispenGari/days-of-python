## Filter Function Python
`filter` is a build in function in python thta allows us to filter collections based on conditions. The filter function accepts 2 parameters which are
* function
  * this function is the first parameter to pass to the filter function. It can be a lambda function or any function that returns a value
* iterable
    * This can be anything a python list, set etc
  
<p align="center">
  <img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
</p>

### Examples
1. filter on sets `lambda-function`:

````python
my_set = {i for i in range(10)}
filtered = filter(lambda x: x % 2 == 0, my_set) ## returns an iterable
print(set(filtered))  ## {0, 2, 4, 6, 8}
````

2. filter on list `lambda-function`:
````python
names = ["name 1", "name 2", "name 3", "name 4", "name 5"]
filtered = filter(lambda x: int(str(x).split(' ')[-1]) % 2 == 0, names) ## returns an iterable
print(list(filtered))

````

3. filter on dict `lambda-function`:
````python
people = [{"name": 1}, {"name": 2}, {"name": 3}, {"name": 4}, {"name": 5}, {"name": 6}]

filtered = filter(lambda x: x["name"] % 2 == 0, people) ## returns an iterable
for person in filtered:
    print(person)
````
#### Defining a function that filters a collection.

1. filtering a dict
````python
people = [{"name": 1}, {"name": 2}, {"name": 3}, {"name": 4}, {"name": 5}, {"name": 6}]
def even(i):
    return i["name"] % 2 == 0

filtered = filter(even, people) ## returns an iterable
for person in filtered:
    print(person)
````

2. filtering a list
````python
names = ["name 1", "name 2", "name 3", "name 4", "name 5"]
def even(i):
    return int(i.split(' ')[-1]) % 2 == 0
filtered = filter(even, names) ## returns an iterable
for person in filtered:
    print(person)

````
3. filtering a set
````python
my_set = {i for i in range(10)}
def even(i):
    return i % 2 == 0
filtered = filter(even, my_set) ## returns an iterable
for person in filtered:
    print(person)
````

> That's it about the filter function.
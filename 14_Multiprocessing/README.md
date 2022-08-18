### Multiprocessing

Multiprocessing refers to the ability of a system to support more than one processor at the same time. Applications in a multiprocessing system are broken to smaller routines that run independently. The operating system allocates these threads to the processors improving performance of the system.

### Why multiprocessing?
Consider a computer system with a single processor. If it is assigned several processes at the same time, it will have to interrupt each task and switch briefly to another, to keep all of the processes going.

### A multiprocessing system can have:

* multiprocessor, i.e. a computer with more than one central processor.
* multi-core processor, i.e. a single computing component with two or more independent actual processing units (called “cores”).
* **Here, the CPU can easily executes several tasks at once, with each task using its own processor.**

To use Multiprocessing in python we import the `multiprocessing` module, which can be imported as follows

```python
import multiprocessing
```

### How can I see how many `cpu` does my computer has?
This is easy, we can use `os` to find the number of cpu for example:

```python
import os
cpu_count = os.cpu_count()
print(f"Number of CPU's in this computer are: {cpu_count}")
```

* Multiprocessing is works the same as Threading the only difference is that Multiprocessing execute more than one thread in parallel. Let's have a look on how Multiprocessing looks in a multi-core computer
 
```python
    
                [-------------------------]
Thread A   ------> [ CORE 1]    [ CORE 2] <----- Thread C
                |                         |
Thread B   ------> [ CORE 3]    [ CORE 4] <----- Theead D
                [-------------------------]
``` 
Here with multi-processing we can execute more than one 
thread without explicitly waiting for other processes to
finish.

### Example of a simple multi-processing example.

* Let's say we have 4 processing that we want to execute simultaneously
we can do it as follows:
  
````python

import multiprocessing, os, time

def process_one(n: int)->None:
    for i in range(n):
        time.sleep(1)
        print(f"Process 1: {i}")

def process_two(n: int)->None:
    for i in range(n):
        time.sleep(1)
        print(f"Process 2: {i}")

def process_three(n: int)->None:
    for i in range(n):
        time.sleep(2)
        print(f"Process 3: {i}")

def process_four(n: int)->None:
    for i in range(n):
        time.sleep(.9)
        print(f"Process 4: {i}")

A = multiprocessing.Process(target=process_one, args=(4, ), name="process1 1")
B = multiprocessing.Process(target=process_two, args=(3, ), name="process1 2")
C = multiprocessing.Process(target=process_three, args=(4, ), name="process1 3")
D = multiprocessing.Process(target=process_four, args=(5, ), name="process1 4")

### Starting the processes

if __name__ == '__main__':
    A.start()
    B.start()
    C.start()
    C.join() # wait until C finishes
    D.start()
````
**Output**

````
Process 2: 0
Process 1: 0
Process 2: 1
Process 3: 0
Process 1: 1
Process 2: 2
Process 1: 2
Process 3: 1
Process 1: 3
Process 3: 2
Process 3: 3
Process 4: 0
Process 4: 1
Process 4: 2
Process 4: 3
Process 4: 4
````

Everything behaves like Threading which was discussed [here](https://github.com/CrispenGari/days-of-python/tree/main/13_Threading).

### A practical Example 
In this section we are going to practically demostrate by use of example how muilti-processing works.

### Checking how many `cpu`'s on a computer using `multiprocessing`
To check the ``cpu`` in `multiprocessing` you can do it as follows:

```py
import multiprocessing as mp
cpu_count = mp.cpu_count()
print(f"CPU count: {cpu_count}")
```

> I have `4` cpu's on my computer.
 
In parallel processing, there are two types of execution: `Synchronous` and `Asynchronous`.

### synchronous execution 
* is when the processes are completed in the same order in which it was started. This is achieved by locking the main program until the respective processes are finished.

### Asynchronous execution
* this doesn’t involve locking. As a result, the order of results can get mixed up but usually gets done quicker.

There are 2 main objects in `multiprocessing` to implement parallel execution of a function: The `Pool` Class and the `Process` Class.

1. Pool Class
   * Synchronous execution
      * `Pool.map()` and `Pool.starmap()`
      * `Pool.apply()`
   * Asynchronous execution
      * `Pool.map_async()` and `Pool.starmap_async()`
      * `Pool.apply_async())`
2. Process Class
We have already looked at this class from the previous examples.

### Using the `Pool` class
We are going to apply use the ``Pool`` class to count how many numbers are present in a given range. First we are 
going to generate random numbers using numpy as follows:

```python
import numpy as np

SEED = 42
np.random.RandomState(SEED)
data = np.random.randint(0, 10, size=[200000, 5]).tolist()
print(data[:5])
```
Solution of our problem without ``parallelization`.

````python
def howmany_within_range(row, minimum, maximum):
    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

start = time.time()
results = []
for row in data:
    results.append(howmany_within_range(row, minimum=4, maximum=8))
print("Took {}s".format(time.time() - start))
````
If we will do it without parallization the output will be as follows:

```shell
Took 0.4497089385986328s
```
The `Pool` class provides some methods to make any function in it like:

1. ``map``
2. ``str_map``
3. ``apply``

The difference between the ``apply`` and `map` functions is that the `apply` takes in `args`
as it's parameter which are the arguments of the function, whilist the ``map`` takes an `iteratable`.

### 1. Pool.apply()
In the following code we are going to perform the same task like before but using parallization method called `apply`

```python

```


### Credits

* [Geeks](https://www.geeksforgeeks.org/multiprocessing-python-set-1/)




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

### Credits

* [Geeks](https://www.geeksforgeeks.org/multiprocessing-python-set-1/)




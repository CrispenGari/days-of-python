### Threading
Threads allow Python programs to handle multiple functions at once as opposed to running a sequence of
commands individually. To use the threading module we have to import it as follows:

```python
import threading
```

What threading essentially does is to execute one task at a time. But the rule is very simple let's say we have 2 threads A and B which are running on a single core as shown below.

````py
    A -----> |---------|
             |  CORE   | <-|
    B -----> |---------|   |
        |__________________|
 (While 'A' is hanged Execute 'B'.)     
````
* Rules are very simple 1 task at a time and a core must be utilized.
* All tasks are executed Sequentially.
* So **How does this works?**
    * Let's say thread 'A' execute a function that allows it to sleep for some seconds.
    * Because A sleeps for some seconds which means there's nothing going on in the CORE for the moment
    which means we can execute B while still waiting for A's sleep seconds to expire then we will execute A.
* **Note:** This applies to more than 1 task, it can be more than 2 threading task.

### Threading method.

1. `threading.active_count()`

Returns the number of active threads in the program.
   
```python
import threading
print(threading.active_count()) # 1 which is the main python file itself
```
2. `threading.current_thread()`

Returns the current threading object.
   
   
```python
import threading, os

current_thread = threading.current_thread()
print(current_thread)  # <_MainThread(MainThread, started 8968)>
```

3. `threading.main_thread()`

Returns the main thread object.

```python
import threading, os
main_thread = threading.main_thread()
print(main_thread)
```
There are a lot of these functions. A list of them are found [here](https://docs.python.org/3/library/threading.html).

And of cause you can name a thread by using a function ``setName(self, name:str)`` for example:

````python
import threading, os
main_thread = threading.main_thread()
main_thread.setName("Main 87")
print(main_thread)
````

### Most important threads function

1 `.start()`

Starts a thread

2. `.join(timeout=None)`

Wait until the thread terminates.
   
3. `run()`

Method representing the thread’s activity.
   
4. `getName()/setName()`

Get/Set the thread name.

5. `.name`

Returns a string of the thread name for example.
```python
import threading, os
main_thread = threading.main_thread()
main_thread.setName("Main 87")
print(main_thread.name) # "Main 87"
```
6. ``.is_alive()->bool``

Return whether the thread is alive. Example
```python
import threading, os
main_thread = threading.main_thread()
main_thread.setName("Main 87")
print(main_thread.is_alive())
```
7. `.daemon`

A boolean value indicating whether this thread is a daemon thread (True) or not (False).

9. `isDaemon() setDaemon()`
Old getter/setter API for daemon; use it directly as a property instead.
   
```python
import threading, os

main_thread = threading.main_thread()
main_thread.setName("Main 87")
print(main_thread.isDaemon())
```


### Examples of Threading.

We are going to have `2` threads A and B.

```python
import threading, os, time

def countA():
    print("A started")
    time.sleep(1)
    print("A finishes")

def countB(n:int)->None:
    print("B started")
    time.sleep(0.5)
    for i in range(n):
        print(i, end=", ")
    print("\nB finishes")

A = threading.Thread(target=countA, name="Thread A")
B = threading.Thread(target=countB, name="Thread B", args=(5, ))

A.start()
B.start()
print("\nWe are done!!")
```

**Output**
```
A started
B started
We are done!!

0, 1, 2, 3, 4, 
B finishes
A finishes
```
### So what is going on here?
1. Thread `A` will run since it is the first thread to be 
called ``A.start()``
2. Because `A` sleeps for a second, then we switch to thread `B` and `B` thread runs. 
3. Because `B` also has a delay of `.5` sec we execute the main thread and print `"We are done!!"`
4. We go back to thread `B` because it's delay expires first and print numbers `0-4`
5. Then we go back to thread `A`.

You have noticed that thread `B` takes `n` as it's argument so 
arguments are then passed as a tuple during the creation of this thread. 
Noticed that we say ``args=(5, )`` That `,` after `5` is neccessary 
because if we don't put it python will interpret `(5)` as `5`.

### `.join()`
This let the thread finish running before moving to another thread. Considering our last example, 
let's say we want to print "We are done!!" after all threads has finnished. We have to call the ``.json`` method 
for both thread for example:

````python
import threading, os, time

def countA():
    print("A started")
    time.sleep(1)
    print("A finishes")

def countB(n:int)->None:
    print("B started")
    time.sleep(0.5)
    for i in range(n):
        print(i, end=", ")
    print("\nB finishes")

A = threading.Thread(target=countA, name="Thread A")
B = threading.Thread(target=countB, name="Thread B", args=(5, ))

A.start()
B.start()
A.join()
B.join()
print("\nWe are done!!")
````

**Output**
```
A started
B started
0, 1, 2, 3, 4, 
B finishes
A finishes
We are done!!
```
Amazing **More** examples.

```python
import threading, os, time

numbers = []
def count(n:int)->None:
    global numbers
    for i in range(n):
        numbers.append(i)

A = threading.Thread(target=count, args=(5, ), name="Thread A")
B = threading.Thread(target=count, name="Thread B", args=(5, ))

A.start()
B.start()
print(numbers)
```
**Output**
```
[0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
```
Thread A will run and and it's numbers from 0 to 4 and B will do the same after thread A finishes. Let's add a delay in our `count` function and see what will be the output.

```python
import threading, os, time

numbers = []
def count(n:int)->None:
    global numbers
    for i in range(n):
        time.sleep(.2)
        numbers.append(i)

A = threading.Thread(target=count, args=(5, ), name="Thread A")
B = threading.Thread(target=count, name="Thread B", args=(5, ))
A.start()
B.start()
B.join()
print(numbers)
```
**Output**
```
[0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
```
Here A will run then B will also run, until all threads finishes.

```python
import threading, os, time

numbers = []
def count(n:int)->None:
    global numbers
    for i in range(n):
        time.sleep(.2)
        numbers.append(i)

A = threading.Thread(target=count, args=(5, ), name="Thread A")
B = threading.Thread(target=count, name="Thread B", args=(5, ))
A.start()
A.join()
B.start()
B.join()
print(numbers)
```
**Output**
```
[0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
```
In this case A will run, because we have called the `A.join()` which means `B` won't run until `A `finishes.
After `A` finishes then `B` will run.

### `.active_count()`
Checking how many active threads are running.
```python
import threading, os, time

numbers = []
def count(n:int)->None:
    global numbers
    for i in range(n):
        time.sleep(.2)
        numbers.append(i)

A = threading.Thread(target=count, args=(5, ), name="Thread A")
B = threading.Thread(target=count, name="Thread B", args=(5, ))
A.start()
B.start()
print(threading.activeCount())
```

**Output**
```
3 # Three threads
```

### Reference
* [Multi Threading](https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/)
* [Ref](https://docs.python.org/3/library/threading.html)
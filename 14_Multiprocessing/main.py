
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


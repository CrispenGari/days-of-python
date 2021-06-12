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
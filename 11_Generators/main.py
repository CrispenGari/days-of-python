

x = (i*i for i in range(5))

while True:
    try:
        print(next(x))
    except StopIteration:
        break
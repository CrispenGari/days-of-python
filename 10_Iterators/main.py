

class xrange:
    def __init__(self, start, stop, step=1):
        self.start = start - step
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration()
        else:
            self.start += self.step
        return self.start


my_range = xrange(0, 10, 2)

while True:
    try:
        print(next(my_range))
    except StopIteration as e:
        print("The iteration runs out of elements")
        break
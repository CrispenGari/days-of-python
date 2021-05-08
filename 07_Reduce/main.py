from functools import reduce

class Number:
    def __init__(self, number):
        self.number = number

numbers = [
    {"number": 1},
    {"number": 2},
    {"number": 3},
    {"number": 4},
    {"number": 5},
]

def add(x, y):
    return x + y.number
sum = reduce(add, [Number(number["number"]) for number in numbers], 0)
print(sum)
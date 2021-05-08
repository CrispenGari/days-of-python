from functools import reduce

numbers = [
    {"number": 1},
    {"number": 2},
    {"number": 3},
    {"number": 4},
    {"number": 5},
]

def add(x, y):
    return x + y["number"]

sum = reduce(add, numbers, 0)
print(sum)
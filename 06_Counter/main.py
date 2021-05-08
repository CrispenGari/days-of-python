from collections import Counter
from random import randrange

numbers = [randrange(0, 4) for i in range(20)]

numbers_dict = Counter(numbers)
print(numbers_dict)
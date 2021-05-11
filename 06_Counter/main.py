from collections import Counter
from random import randrange

numbers = [randrange(0, 4) for i in range(20)]

counter = Counter()
for number in numbers:
    counter[number] += 1

print(counter.most_common(2))
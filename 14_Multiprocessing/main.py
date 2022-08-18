import multiprocessing as mp
import numpy as np
import time

cpu_count = mp.cpu_count()

SEED = 42
np.random.RandomState(SEED)
data = np.random.randint(0, 10, size=[200000, 5]).tolist()
print(data[:5])

def howmany_within_range_rowonly(row, minimum=4, maximum=8):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

pool = mp.Pool(mp.cpu_count())

results = pool.map(howmany_within_range_rowonly, [row for row in data])

pool.close()

print(results[:10])
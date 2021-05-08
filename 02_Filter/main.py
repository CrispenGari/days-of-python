
my_set = {i for i in range(10)}
names = ["name 1", "name 2", "name 3", "name 4", "name 5"]
people = [{"name": 1}, {"name": 2}, {"name": 3}, {"name": 4}, {"name": 5}, {"name": 6}]

def even(i):
    return int(i.split(' ')[-1]) % 2 == 0
filtered = filter(even, names) ## returns an iterable
for person in filtered:
    print(person)

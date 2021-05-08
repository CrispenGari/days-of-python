

my_list = ["name1", "name2", "name3", "name4", "name5"]

def upper(i):
    return i.upper()
res = map(upper, my_list)
print(list(res))
from collections import OrderedDict

my_dict = OrderedDict()

for i in range(10):
    my_dict[i] = i**2

for i in range(10):
    print(my_dict[i])
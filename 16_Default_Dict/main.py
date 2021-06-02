from collections import defaultdict

default_dict = defaultdict(int, {
    "name": "Hello",
    "age" : 21,
    "yob": 2001
})
print(f"Name: {default_dict['name']}, Age: {default_dict['age']}, YOB: {default_dict['yob']}, Gender: {default_dict['gender']}")
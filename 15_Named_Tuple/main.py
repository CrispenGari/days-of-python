from collections import namedtuple
Module = namedtuple("Module",
                    ["name", "code"]
                    )
Student = namedtuple(
    "Student",
    ["name", "age", "module"]
)
names = ["Name1", "Name2", "Name3", "Name4"]
modules = ["IT", "DS", "AI", "ML"]
students = []
for name, module in zip(names, modules):
    students.append(Student(name, 21, Module(module, 221)))
for student in students:
    print(f"Name: {student.name}, Age: {student.age}, Module Name: {student.module.name}, Module Code: {student.module.code}")
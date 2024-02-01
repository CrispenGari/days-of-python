from abc import abstractmethod, ABCMeta


class IDepartment(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, employees):
        """To be implemented"""

    @staticmethod
    @abstractmethod
    def print_department():
        """"""


class Testing(IDepartment):
    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Testing: {self.employees}")


class Deploying(IDepartment):
    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Development: {self.employees}")


class Development(IDepartment):
    def __init__(self, employees):
        self.employees = employees
        self.deps = list()
        self.all_employees = employees

    def add_department(self, dep):
        self.deps.append(dep)
        self.all_employees += dep.employees

    def print_department(self):
        print(f"Department Employees: {self.all_employees}")
        for dep in self.deps:
            dep.print_department()
        print(f"Total Employees: {self.employees}")


dep = Development(15)
dep.add_department(Testing(10))
dep.add_department(Deploying(3))
dep.print_department()

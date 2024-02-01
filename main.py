from abc import abstractmethod, ABCMeta


class IUser(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def hi(self, name: str) -> str:
        """This is hi menthod"""


class Student(IUser):
    def hi(self, name):
        print("Student {name}".format(name=name))


class Manager(IUser):
    def hi(self, name):
        print("Manager {name}".format(name=name))


class Other(IUser):
    def hi(self, name):
        print("Other {name}".format(name=name))


class UserFactory:
    @staticmethod
    def get_user(type: str):
        if type.lower() == "student":
            return Student()
        if type.lower() == "manager":
            return Manager()
        return Other()


UserFactory.get_user("student").hi("Bob")
UserFactory.get_user("manager").hi("Bob")
UserFactory.get_user("haha").hi("Bob")

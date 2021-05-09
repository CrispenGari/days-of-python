
class Dog:
    def __init__(self):
        pass
    @staticmethod
    def greater(a):
        return a > 6
    @classmethod
    def printHello(cls, name):
        print("Hello " + name)
Dog.printHello("Dog")
print(Dog.greater(45))

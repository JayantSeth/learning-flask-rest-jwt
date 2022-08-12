# Learning property
'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        print("Getting name...")
        return self._name

    @name.setter
    def name(self, value):
        print("setting name...")
        self._name = value

    @property
    def age(self):
        print("Getting age...")
        return self._age

    @age.setter
    def age(self, value):
        print("Setting age...")
        self._age = value


std1 = Student("jayant", 28)

std1.name = "Jayant"

std1.age = 29
'''

# Learning Decorators


def make_lower(func):
    def inner():
        apple="Apple"
        print("Running lower")
        stuff = func(apple)
        return stuff.lower()
    return inner


@make_lower
def ordinary(apple):
    return f"This is ORDINARY {apple}"


print(ordinary())


def smart_devision(func):
    def inner(a, b):
        if b == 0:
            return "Devisor cannot be zero"
        return func(a, b)
    return inner


@smart_devision
def devide(a, b):
    return a/b


print(devide(10, 10))

# lower = make_lower(ordinary)

# print(lower())


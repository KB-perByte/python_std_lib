# day - 3

class Person:
    def __init__(self, *args, **kwargs):
        print(f"Person called {args}, {kwargs}")

class Student(Person):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        print(f"Student called {args}, {kwargs}")

student = Student(school_name = "Westmont Hight", name = "Joe")
#129. Create an object in a class


class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show(self):
        print("Name:", self.name, "Roll:", self.roll)


name = input("Enter student name: ")
roll = int(input("Enter roll number: "))

s1 = Student(name, roll)
s1.show()

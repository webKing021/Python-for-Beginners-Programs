# ===============================
# 🧠 Object-Oriented Programming (OOP) Concepts in Python
# ===============================

# Class -> Blueprint or template of object
# Object -> Instance of class (real-world entity)
# Attributes -> Properties of object
# Methods -> Actions or behaviors of object
# self -> Refers to the current instance of class
# Constructor -> Special method (__init__), initializes attributes
# Inheritance -> One class acquires properties of another
# Polymorphism -> One interface, multiple implementations
# Encapsulation -> Hiding data and implementation details
# Abstraction -> Showing essential features, hiding complexity
# Operator Overloading -> Defining custom behavior for operators
# Method Overloading -> Same method, different parameters (simulated)
# Method Overriding -> Redefining a method in subclass

# ===============================
# Libraries
# ===============================
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# matplotlib -> data visualization
# numpy -> numerical operations
# pandas -> data analysis

# ===============================
# Example 1: Basic Class and Object
# ===============================
class Student:
    name = {"XYZ": "KRUTARTH"}  # class attribute (dictionary)

# Access class attribute
print(Student.name)

# Create object
std = Student()
print(std.name)

# Check types
print(type(std))
print(type(Student()))

# Instance attribute shadowing
std.name = "abc"
print(std.name)       # instance value
print(Student.name)   # class value

# Modify class attribute (works because it's a dict)
Student.name["XYZ"] = "ABC"
print(Student.name)

# ===============================
# Example 2: Constructor and Class Variable
# ===============================
class Student2:
    count = 0  # class variable to count instances

    def __init__(self):
        Student2.count += 1

# Initially
print(Student2.count)

# Create objects
std2_1 = Student2()
std2_2 = Student2()

# After creating 2 objects
print(Student2.count)

# ===============================
# Example 3: Inheritance and Method Overriding
# ===============================
class Person:
    def show(self):
        print("I am a Person")

class Teacher(Person):
    def show(self):
        print("I am a Teacher (Overridden Method)")

p1 = Person()
t1 = Teacher()
p1.show()
t1.show()

# ===============================
# Example 4: Polymorphism
# ===============================
def display_role(obj):
    obj.show()

display_role(p1)
display_role(t1)

# ===============================
# Example 5: Encapsulation
# ===============================
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute (name mangling)

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = Account("John", 1000)
acc.deposit(500)
print(acc.get_balance())

# Accessing private variable directly will fail:
# print(acc.__balance)  # ❌ AttributeError

# ===============================
# Example 6: Abstraction
# ===============================
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print("Area of Circle:", c.area())

# ===============================
# Example 7: Operator Overloading
# ===============================
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
print(p1 + p2)

# ===============================
# Example 8: Method Overloading (Simulated using default args)
# ===============================
class Calculator:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        else:
            return a

calc = Calculator()
print(calc.add(2, 3))
print(calc.add(2, 3, 4))

# ===============================
# ✅ End of OOP Demonstration
# ===============================

# Write a python program to print area and circumference of circle using module
# module
import Circle

print(Circle.area(5))
print(Circle.circumference(5))
print(Circle.volume(5))

# alias name of module
import Circle as C

print(C.area(5))
print(C.circumference(5))
print(C.volume(5))

# from module import function
from Circle import area

print(area(5))

# from module import all functions
from Circle import *

print(area(5))
print(circumference(5))
print(volume(5))

# colifier
from Circle, math
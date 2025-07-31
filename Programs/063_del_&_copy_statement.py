# del statement means delete the list
s = [1, 2, 3, 4, 5]
del s[0]
del s[1:3]
del s
print(s)

# copy / clone statement
# eg: 1 by copy() method
str1 = [1, 2, 3, 4, 5]
s1 = str1.copy()
print(s1)

# eg: 2 by slice operator
str1 = [1, 2, 3, 4, 5]
s1 = str1[:]
print(s1)

# eg: 3 by list() function
str1 = [1, 2, 3, 4, 5]
s1 = list(str1)
print(s1)

# eg: 4 by extend() method
str1 = [1, 2, 3, 4, 5]
s1 = []
s1.extend(str1)
print(s1)

# eg: 5
a = str1
print(a)


# shallow copy
# A shallow copy makes a new outer object (like a list or dictionary),
# but it doesn’t copy the inside things (like lists inside a list).
# Instead, it just points to the same inner objects.
# So if you change something inside (like a list inside a list),
# both the original and the copy will change.

# eg: 1 by copy() method
original = [1, 2, [3, 4]]
shallow = original.copy()

shallow[2][0] = 99
print("Original:", original)
print("Shallow:", shallow)

# eg: 2 by slice operator
original = [1, 2, [3, 4]]
shallow = original[:]

shallow[2][0] = 99
print("Original:", original)
print("Shallow:", shallow)

# eg: 3 by list() function
original = [1, 2, [3, 4]]
shallow = list(original)

shallow[2][0] = 99
print("Original:", original)
print("Shallow:", shallow)

# eg: 4 by extend() method
original = [1, 2, [3, 4]]
shallow = []
shallow.extend(original)

shallow[2][0] = 99
print("Original:", original)
print("Shallow:", shallow)



# Deep Copy
# A deep copy creates a completely independent copy of an object, including all nested (inner) objects.
# That means changes made to the original object's inside elements will NOT affect the deep copy, and vice versa.
# It's like cloning not just a box, but also cloning everything inside the box.

# 🛠️ Syntax:
# To make a deep copy, you need to use the copy module:
# import copy

# deep_copy_object = copy.deepcopy(original_object)

# eg: 1
import copy

original = [1, 2, [3, 4]]
deep = copy.deepcopy(original)

deep[2][0] = 99
print("Original:", original)
print("Deep:", deep)

# | Feature        | Shallow Copy              | Deep Copy                  |
# | -------------- | ------------------------- | -------------------------- |
# | Outer object   | New object                | New object                 |
# | Nested objects | Same as original (shared) | Fully copied (independent) |
# | Module used    | `copy.copy()`             | `copy.deepcopy()`          |

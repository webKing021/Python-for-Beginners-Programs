# i.) How to find the number of elements in the list?
l = [1, 2, 3, 4]
len(l)  

# ii.) How to find the largest and lowest value in the list?
max(l)  
min(l)  

# iii.) How to check whether the list is empty or not?
if not l:
    print("List is empty")
else:
    print("List is not empty")

# iv.) How to find the first and last element of the list?
l[0]  
l[-1]  

# v.) How to access an element of the list?
l[2]  

# vi.) How to modify an element of the list?
l[2] = 10
l

# vii.) How to concatenate 2 lists?
l1 = [1, 2, 3]
l2 = [4, 5, 6]
a = l1 + l2
a

# viii.) How to add 2 lists element-wise in Python?
l1 = [1, 2, 3]
l2 = [4, 5, 6]
a = [x + y for x, y in zip(l1, l2)]
a

# ix.) How to remove duplicate elements in the list?
l = [1, 2, 3, 4, 1, 2, 3]
list(set(l))

l2 = []
for i in l:
    if i not in l2:
        l2.append(i)
l2

# x.) How to find the occurrences of an element in the Python list?
l = [1, 2, 3, 4, 1, 2, 3]
l.count(1)

# xi.) How to find the index of an element in the Python list?
l.index(1)

# xii.) How to check if an item is in the list?
if 1 in l:
    print("Found")
else:
    print("Not Found")

# xiii.) How to insert an item at a given position?
l.insert(2, 10)
l

# xiv.) How to flatten a list in Python?
l = [[1, 2], [3, 4], [5]]
a = [i for j in l for i in j]
a

# xv.) How to convert Python list to other data structures like set, tuple, dictionary?
l = [1, 2, 3, 4]
set(l)
tuple(l)
dict(l)

# xvi.) How to apply a function to all items in the list?
s = [x**2 for x in l]
s

# xvii.) How to filter elements based on a function in Python list?
l = [1, 2, 3, 4, 5, 6]
a = [x for x in l if x % 2 == 0]
a

# xviii.) How Python lists are stored in memory?
# Python lists are dynamic arrays.
# They store references (pointers) to the actual objects, not the objects themselves.
# The list has extra allocated space to allow growth without reallocating memory each time.
# Internally, lists are implemented as a contiguous block of memory holding pointers to objects.
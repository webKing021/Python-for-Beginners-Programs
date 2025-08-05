# tuple
# tuple is a collection of items that are ordered and unchangeable.
# In Python, tuples are written with round brackets.

t = ()
print(t)

print(type(t))

# to create int tuple
t1 = (1, 2, 3, 4, 5)
print(t1)
len(t1)

# tuple with mix data types
t2 = (21,"krutarth", 9.29)
print(t2)

# nested tuple
t3 = ("krutarth", [1,2,3], (4,5,6))
print(t3)

# tuple without parenthesis
t4 = 21, "krutarth", 9.29
print(t4)

# singleton tuple
t5 = ("krutarth",)
print(t5)

# nested tuple with singleton tuple
t6 = ("krutarth", (1,2,3), [4,5,6])
print(t6[0][3])
print(t6[1][2])
print(t6[2][1])


# tuple unpacking
t7 = (1,2,3)
a,b,c = t7
print(a)
print(b)
print(c)

# singleton tuple can also create without parenthesis
t8 = 1,
print(t8)
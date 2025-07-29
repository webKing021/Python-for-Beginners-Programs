# String operations

# null str
str = ""
print(f"Empty string: {str}")

# not null
s1 = "python"
print(len(s1))

# accessing character by index
x = s1[3]
print(f"Character at index 3: {x}")

# range print
x = s1[0:2]
print(f"Characters from index 0 to 1: {x}")

# concat
s2 = " krutarth"
x = s1 + s2
print(f"Concatenated string: {x}")

# multiply
x = 5 * s1
print(f"String multiplied by 5: {x}")

# Membership operator
e = "y"
s1 = "python"
if (e in s1):
    print(s1)
else:
    print("ELSE")

# NOT membership op
e = "y"
if (e not in s1):
    print(s1)
else:
    print("ELSE")

# split
s3 = "21, Krutarth, R"
x = s3.split(", ")
print(x)

# space will not split
s3 = "21 Krutarth R"
x = s3.split()
print(x)

# count
s = "krutarth is good, het is good, krutarth is good"
x = "krutarth"
print(s.count(x))

# Counting individual characters
print("\n# Counting individual characters")
a = s.count("a")
b = s.count("i")
c = s.count("o")
d = s.count("e")
e = s.count("u")
print(f"a = {a}")
print(f"i = {b}")
print(f"o = {c}")
print(f"e = {d}")
print(f"u = {e}")


# String is Immutable
s = "Hello, Krutarth"
s[0] = 'h'                  # this will throw an error as string is immutable
print(s)

# Mutability
s = "Hello, Krutarth"
s = "Hello, Python"
print(s)

# Multiline String (Docstring)
s = '''Hello, Krutarth
I am a Python Programmer'''
print(s)

s = """Hello, Krutarth
I am a Python Programmer"""
print(s)

s = "Hello, \
Krutarth"
print(s)
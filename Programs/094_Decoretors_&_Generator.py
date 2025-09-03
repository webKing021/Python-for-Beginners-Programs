# Decorators
def null_deco(func):
    return func

def greet():
    return "Hello"

g = null_deco(greet)

@null_deco
def greet():
    return "Hello"

print(greet())

# Generator
def gfunc():
    yield 1
    yield 2
    yield 3

for v in gfunc():
    print(v)

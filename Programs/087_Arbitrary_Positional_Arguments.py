# Arbitrary Positional Arguments

def fun(*argv):
    for arg in argv:
        print(arg)

fun("Hello", "Krutarth")

# Arbitrary Keyword Arguments
def fun1(**kwargs):
    for k,v in kwargs.items():
        print("%s == %s" % (k,v))

fun1(name="Krutarth", age=21)
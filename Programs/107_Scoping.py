#Scoping
def fun(x):
    y = 1
    x = x + y
    print("Inner x is =",x)
    return x
x = 3
y = 2
z = fun(x)
print("x =",x)
print("y =",y)
print("z =",z)

#Local Scoping
def fun(x,y):
    a = 42
    x,y = y,x
    b = 33
    b = 17
    c = 100
    print(a,b,x,y)

a,b,x,y = 1,15,3,4
fun(17,4)
print(a,b,x,y)

#Global Scoping
def fun(x,y):
    global a
    a = 42
    x,y = y,x
    b = 33
    b = 17
    c = 100
    print(a,b,x,y)

a,b,x,y = 1,15,3,4
fun(17,4)
print(a,b,x,y)

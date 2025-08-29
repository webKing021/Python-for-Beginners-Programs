# 1. normal Functions
def get_max(a,b):
    x = 10
    y = 10
    if x > y:
        print("x is greater")
    else:
        print("y is greater")

# call by value       
get_max(10,20)

# show type of function
print(type(get_max))


# 2. User-input Functions
def get_max():
    x = int(input("Enter num1 : "))
    y = int(input("Enter num2 : "))
    if x > y:
        print("max : ", x)
    else:
        print("max : ", y)

get_max()
        
# 3. Parameterized Functions
def get_max(a,b):
    if a > b:
        print("max : ", a)
    else:
        print("max : ", b)

get_max(10,20)

# 4. return value
def get_max(a,b):
    if a > b:
        return a
    else:
        return b

x=int(input("Enter num1 : "))
y=int(input("Enter num2 : "))
z = get_max(x,y)
# z = get_max(y=x, x=y)
# print("max : ", z)
print("max : ", get_max(x,y))


# 5. 3 agrs with default parameters
def get_name(lname, fname, flag = True):
    if flag:
        print("Name : ", fname, lname)
    else:
        print("Name : ", lname, fname)      

get_name("Krutarth", "Raychura", False)
get_name("Krutarth", "Raychura")
get_name("Krutarth", "Raychura", True)


# 6. advance concept of default args
def get_no(x, y=1, z):  # this will throw error because z is not default and after any default arg, all args must be default
    print(x + y + z)

get_no(10)
get_no(10,20)
get_no(10,20,30)
get_no(7, z=2)
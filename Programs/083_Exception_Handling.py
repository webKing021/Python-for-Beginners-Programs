# exception handling
try:
    #code
    x = 100
    y = 1
    print(x/y)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("No error")
finally:
    print("This will always execute")


# 1 - built in exception and multiple except blocks
try:
    # print(10/0)
    l1 = [1,2,3]
    print(l1[3], x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except IndexError:
    print("Index out of range")
except NameError:
    print("Variable not defined")
except (ZeroDivisionError, IndexError, NameError):
    print("Multiple exceptions")
else:
    print("No error")
finally:
    print("This will always execute")


# 2 - user defined exception
class InvaildAgeException(Exception):
    "Age 18 se kam hai."
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise InvaildAgeException
    else:
        print("eligible to vote")
except InvaildAgeException:
    print("invaild age")
except NameError:
    print("Name error")


# 3 - auto exception / Exception Aliasing
try:
    print(10/0,x)
except Exception as e:
    print(e)


# 1. Function Facts
def f1():
    pass

f1                  # function f1 at memory location/address
f1()                # calling function
del f1              # delete function  
print(id(f1))       # id of function


# 2. WAP to perform Magic Method.
f1.__name__

# 3. function in list
x = [f1, 1, 2]

# 4. function in dictionary
x = {f1: 1, 2: 3}

# 5. WAP to demonstrate function as argument.
def cal(a,b):
    a = a + b
    s = a - b
    return a, s

a, b = cal(12,21)

# 6. WAP to demonstrate function can call another function
def yell(text):
    return text.upper() + "!"

def greet(func):
    greeting = func("Krutarth")
    print(greeting)

print(greet(yell))      # this will print "KRUTARTH!" also print None
greet(yell)             # this will print "KRUTARTH!" but not print None


# 7. WAP to demonstrate nested function.
def speak(text):
    def whisper(t):
        return t.lower() + "...."
    return whisper(text)

print(speak("Krutarth"))
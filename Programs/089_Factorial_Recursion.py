# Factorial using recursion

def fact(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * fact(n - 1)

print(fact(5))

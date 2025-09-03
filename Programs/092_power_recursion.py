# Power calculation using recursion
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = power(base, exp)
print(f"{base}^{exp} = {result}")

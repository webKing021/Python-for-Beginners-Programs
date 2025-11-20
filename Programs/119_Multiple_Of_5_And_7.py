#119. Check whether the given integer is a multiple of both 5 and 7

n = int(input("Enter an integer: "))

if n % 35 == 0:
    print(n, "is a multiple of both 5 and 7")
else:
    print(n, "is not a multiple of both 5 and 7")

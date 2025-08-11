# WAP to take User-Input n terms & print n: n * 5
n = int(input("Enter n terms: "))
d = {n: n*5 for n in range(1, n+1)}
print(d)
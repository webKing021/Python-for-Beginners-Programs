#120. Display all integers between 100 and 200 whose sum of digits is even

print("Numbers between 100 and 200 with even digit sum:")
for n in range(100, 201):
    s = 0
    temp = n
    while temp > 0:
        s += temp % 10
        temp //= 10
    if s % 2 == 0:
        print(n)

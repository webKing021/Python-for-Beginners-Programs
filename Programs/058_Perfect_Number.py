# WAP to check if a number is perfect or not

n = int(input("Enter a number: "))

sum = 0
for i in range(1, n):
    if n % i == 0:
        sum += i

if sum == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")

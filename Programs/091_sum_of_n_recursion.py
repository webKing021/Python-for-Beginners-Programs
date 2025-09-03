# Sum of n natural numbers using recursion
def sum_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_n(n-1)

num = int(input("Enter number: "))
result = sum_n(num)
print(f"Sum of first {num} natural numbers: {result}")

# WAP to Print Pascal's Triangle & Also Write an Algorithem for it
from math import factorial

n = 5
for i in range(n):
    for j in range(n - i + 1):
        # left padding
        print(end=" ")

    for j in range(i + 1):
        # nCr = n! / (r! * (n-r)!) 
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
    # for new line
    print()


# Algorithm:

# Take a number of rows to be printed, lets assume it to be n
# Make outer iteration i from 0 to n times to print the rows.
# Make inner iteration for j from 0 to (N - 1).
# Print single blank space " ".
# Close inner loop (j loop) //its needed for left spacing.
# Make inner iteration for j from 0 to i.
# Print nCr of i and j.
# Close inner loop.
# Print newline character (\n) after each inner iteration.
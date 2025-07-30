# WAP to print a diamond pattern

n = int(input("Enter a number: "))

# Upper half of diamond
for i in range(n):
    # Print spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # Print stars    
    for j in range(2 * i + 1):
        print("*", end="")
    print()

# Lower half of diamond
for i in range(n-2, -1, -1):
    # Print spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # Print stars
    for j in range(2 * i + 1):
        print("*", end="")
    print()
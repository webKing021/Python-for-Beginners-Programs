# Fibonacci

num = int(input("Enter the number of terms: "))

n1 = 0 
n2 = 1

for i in range(num): 
    print(n1)   
    n1, n2 = n2, n1 + n2 

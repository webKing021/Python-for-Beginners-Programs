# List Comprehensions means writing code in a single line / concise way
s = []
for x in range(10):
    s.append(x ** 2)
print(s)

# List Comprehensions
s = [x ** 2 for x in range(10)]     
print(s)

# eg : 1
# Define the matrix first
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Transpose the matrix using list comprehension
s = [[row[i] for row in matrix] for i in range(4)]
print(s)

# eg : 2
l = [[row[i] for row in matrix] for i in range(4)] + \
 [[row[i] for row in matrix] for i in range(3)]
print(l)

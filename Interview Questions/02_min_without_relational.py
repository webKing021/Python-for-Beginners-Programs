"""
Find minimum among two numbers without using relational operators
"""

def minimum(a, b):
    return (a + b - abs(a - b)) // 2

print("Minimum is:", minimum(10, 25))  # Output: 10

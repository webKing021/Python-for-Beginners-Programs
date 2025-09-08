"""
Add two numbers without using arithmetic operators
"""

def add(a, b):
    # Iterate till there is no carry
    while b != 0:
        # carry now contains common set bits of a and b
        carry = a & b

        # Sum of bits where at least one of the bits is not set
        a = a ^ b

        # Carry is shifted by one so that adding it to a gives the required sum
        b = carry << 1

    return a

x = 15
y = 27
print("Sum:", add(x, y))  # Output: 42

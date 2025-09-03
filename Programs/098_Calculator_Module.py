# Write a python program to create a calculator using module.
# Calculator module
import Calculator as C
print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice (1-4): "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Result:", C.add(a, b))
elif choice == 2:
    print("Result:", C.subtract(a, b))
elif choice == 3:
    print("Result:", C.multiply(a, b))
elif choice == 4:
    print("Result:", C.divide(a, b))
else:
    print("Invalid choice")

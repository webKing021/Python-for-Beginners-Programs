#117. Print all possible combinations from three digits

a = int(input("Enter first digit: "))
b = int(input("Enter second digit: "))
c = int(input("Enter third digit: "))

digits = [a, b, c]

print("All possible combinations:")
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and i != k:
                print(digits[i], digits[j], digits[k])

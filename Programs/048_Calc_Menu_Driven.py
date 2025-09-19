# simple user input calculator by creating menu

ch = 9
while(ch != 5):
    print("**** Menu ****")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    ch = int(input("Enter your choice: "))
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if(ch == 1):
        print(num1 + num2)
    elif(ch == 2):   
        print(num1 - num2)
    elif(ch == 3):  
        print(num1 * num2)
    elif(ch == 4):
        print(num1 / num2)
    elif(ch == 5):
        print("Exit")
    else:
        print("Invalid choice")
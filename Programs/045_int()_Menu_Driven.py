# menu driven program for binary, octal, hexa, 32 to decimal

ch = 9
while(ch != 5):
    print("Menu")
    print("1. Binary to Decimal")
    print("2. Octal to Decimal")
    print("3. Hexa to Decimal")
    print("4. Base-32 to Decimal")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if(ch == 1):
        num = input("Enter binary number: ")
        print(int(num, 2))  
    elif(ch == 2):
        num = input("Enter octal number: ")
        print(int(num, 8))  
    elif(ch == 3):
        num = input("Enter hexadecimal number: ")
        print(int(num, 16))  
    elif(ch == 4):
        num = input("Enter base-32 number: ")
        print(int(num, 32))  
    elif(ch == 5):
        print("Exit")
    else:
        print("Invalid choice")
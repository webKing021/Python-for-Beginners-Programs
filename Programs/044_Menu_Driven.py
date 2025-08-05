# menu driven programing for Decimal to binary, octal, hexa, 32

ch = 9
while(ch != 5):
    print("Menu")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexa")
    print("4. Exit")

    ch = int(input("Enter your choice: "))
    
    if(ch == 1):
        num = int(input("Enter decimal number: "))
        print(bin(num)) 
    elif(ch == 2):
        num = int(input("Enter decimal number: "))
        print(oct(num)) 
    elif(ch == 3):
        num = int(input("Enter decimal number: "))
        print(hex(num))  
    elif(ch == 4):
        print("Exit")
    else:
        print("Invalid choice")

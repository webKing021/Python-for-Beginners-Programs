# WAP a menu driven program to check entered number is :
# a palindrome
# armstrong number
# reverse number
# display number of digits without using len() 
# sum of digits 
# exit

ch = 7
while ch != 6:
    print("1. Palindrome")
    print("2. Armstrong Number")
    print("3. Reverse Number")
    print("4. Number of Digits")
    print("5. Sum of Digits")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if (ch == 1):
        n = int(input("Enter a number: "))
        if n == n[::-1]:
            print("Palindrome")
        else:
            print("Not Palindrome")

    elif (ch == 2):
        num = int(input("Enter a number: "))
        sum = 0
        temp = num

        while temp > 0:
            digit = temp % 10
            sum = sum + digit * digit * digit
            temp = int(temp / 10)  

        if num == sum:
            print(f"{num} is an Armstrong number")
        else:
            print(f"{num} is not an Armstrong number")
         
    elif (ch == 3):
        n = int(input("Enter a number: "))
        r = int(str(n)[::-1])
        print("Reverse Number:", r)
        
    elif (ch == 4):
        n = int(input("Enter a number: "))
        count = 0
        while n > 0:
            n = n // 10
            count += 1
        print("Number of Digits:", count)

    elif (ch == 5):
        n = int(input("Enter a number: "))
        sum = 0
        while n > 0:
            sum = sum + n % 10
            n = n // 10
        print("Sum of Digits:", sum)

    elif (ch == 6):
        print("Exit")

    else:
        print("Invalid Choice")

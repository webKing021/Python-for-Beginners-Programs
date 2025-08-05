t = (1, 2, 3, 4, 5)
ch = 9

while (ch != 0):
    print("1. Display")
    print("2. Add")
    print("3. Delete")
    print("4. Update")
    print("0. Exit")
    ch = int(input("Enter your choice: "))

    if (ch == 1):
        print(t)
    elif (ch == 2):
        x = int(input("Enter element to add: "))
        y = int(input("Enter index: "))
        t1 = t[:y]
        t2 = t[y:]
        t = t1 + (x, ) + t2
        print(t)

    elif (ch == 3):
       i = int(input("Enter index: "))
       t = t[:i] + t[i+1:]
       print(t)
    elif (ch == 4):
        i = int(input("Enter index: "))
        x = int(input("Enter element to update: "))
        t = t[:i] + (x, ) + t[i+1:]
        print(t)
    elif (ch == 0):
        print("Exit")
    else:
        print("Invalid choice")

        


#  Menu-Driven Dictionary CRUD program in Python [Create/Add, Read/Display, Update, Delete]
d = {}
ch = 9
while (ch != 5):
    print("1. Add")
    print("2. Display")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if (ch == 1):
        n = int(input("Enter no. of elements: "))
        for i in range(n):
            k = input("Enter key: ")
            v = input("Enter value: ")
            d[k] = v
    elif (ch == 2):
        print(d)
    elif (ch == 3):
        k = input("Enter key to update: ")
        v = input("Enter new value: ")
        d[k] = v
    elif (ch == 4):
        k = input("Enter key to delete: ")
        d.pop(k)
    elif (ch == 5):
        break
    else:
        print("Invalid Choice")

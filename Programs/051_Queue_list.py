q = []
ch = 4

while(ch != 0):
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("0. Exit")

    ch = int(input("Enter your choice: "))  
    if ch == 1:
        q.append(int(input("Enter element: ")))
        print(q)
    elif ch == 2:
        q.pop(0)
        print(q)
    elif ch == 3:
        print(q)
    elif ch == 0:
        print("Exit")
    else:
        print("Invalid choice")

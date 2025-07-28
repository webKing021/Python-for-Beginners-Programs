s = []
ch = 4

while(ch != 0):
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("0. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        s.append(int(input("Enter element: ")))
        print(s)
    elif ch == 2:
        s.pop()
        print(s)
    elif ch == 3:
        print(s)
    elif ch == 0:
        print("Exit")
    else:
        print("Invalid choice")
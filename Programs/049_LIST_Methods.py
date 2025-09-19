l = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]

ch = 13
while (ch != 12):
    print("MENU")
    print("1. Display list elements")
    print("2. Add element to list")
    print("3. Remove element from list")
    print("4. Length of list")
    print("5. Count of element in list")
    print("6. Sort list")
    print("7. Reverse list")
    print("8. Index of element")
    print("9. Pop element from list")
    print("10. Insert element at index")
    print("11. Extend list")
    print("12. Exit")

    ch = int(input("Enter your choice: "))
    if ch == 1:
        print(l)
    elif ch == 2:
        l.append(int(input("Enter element to add: ")))
        print(l)
    elif ch == 3:
        l.remove(int(input("Enter element to remove: ")))
        print(l)
    elif ch == 4:
        print(len(l))
    elif ch == 5:
        print(l.count(int(input("Enter element to count: "))))
    elif ch == 6:
        l.sort()
        print(l)
    elif ch == 7:
        l.reverse()
        print(l)
    elif ch == 8:
        print(l.index(int(input("Enter element to find index: "))))
    elif ch == 9:
        l.pop()
        print(l)
    elif ch == 10:
        l.insert(int(input("Enter index: ")), int(input("Enter element: ")))
        print(l)
    elif ch == 11:
        l.extend(l2)
        print(l)
    elif ch == 12:
        print("Exit")
    else:
        print("Invalid choice")
    

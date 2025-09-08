# File CURD Menu
ch = 9
while(ch != 5):
    print("Menu")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if(ch == 1):
        f = open("emp.txt","a")
        for i in range(1):
            eno = input("Enter the empno:")
            ename = input("Enter the empname:")
            esal = input("Enter the empsal:")
            f.write(str(eno)+","+str(ename)+","+str(esal)+"\n")
        f.close()

    elif(ch == 2):
        f = open("emp.txt","r")
        for i in f:
            print(i)
        f.close()

    elif(ch == 3):
        eno = input("Enter the empno to update:")
        sal = input("Enter the new salary:")
        f = open("emp.txt","r")
        fnew = open("emp1.txt","w")
        for i in f:
            f1,f2,f3 = i.split(",")
            if f1 == eno:
                fnew.write(f1+","+f2+","+sal+"\n")
            else:
                fnew.write(i)
        f.close()
        fnew.close()  

    elif (ch == 4):
        eno = input("Enter the empno to delete:")
        f = open("emp1.txt", "r")
        fnew = open("emp.txt", "w")
        for i in f:
            f1,f2,f3 = i.split(",")
            if f1 == eno:
                print(f1, " is deleted")
            else:
                fnew.write(i)
        f.close()
        fnew.close()

    elif(ch == 5):
        print("Exit")
        
    else:
        print("Invalid choice")
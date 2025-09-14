# File CURD Menu (Binary Mode)
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
        f = open("emp.txt","ab")  # Open in binary append mode
        for i in range(1):
            eno = input("Enter the empno:")
            ename = input("Enter the empname:")
            esal = input("Enter the empsal:")
            line = str(eno)+","+str(ename)+","+str(esal)+"\n"
            f.write(line.encode('utf-8'))  # Encode string to bytes
        f.close()

    elif(ch == 2):
        f = open("emp.txt","rb")  # Open in binary read mode
        for i in f:
            print(i.decode('utf-8').strip())  # Decode bytes to string and strip newline
        f.close()

    elif(ch == 3):
        eno = input("Enter the empno to update:")
        sal = input("Enter the new salary:")
        f = open("emp.txt","rb")
        fnew = open("emp1.txt","wb")
        for i in f:
            line_str = i.decode('utf-8')  # Decode bytes to string
            f1,f2,f3 = line_str.split(",")
            if f1 == eno:
                new_line = f1+","+f2+","+sal+"\n"
                fnew.write(new_line.encode('utf-8'))
            else:
                fnew.write(i)  
        f.close()
        fnew.close()  

    elif (ch == 4):
        eno = input("Enter the empno to delete:")
        f = open("emp1.txt", "rb")  
        fnew = open("emp.txt", "wb")
        for i in f:
            line_str = i.decode('utf-8')
            f1,f2,f3 = line_str.split(",")
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

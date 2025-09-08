# files 
f = open("stu.txt", "r")
for i in f:
    print(i)
    name, m1, m2, m3 = i.split(",")
    print(name, m1, m2, m3)
    if min(m1, m2, m3) < 35:
        print(f"{name} is failed")
    else:
        print(f"{name} is passed")
f.close()

# files objects
f.name
f.mode
f.close()
f.errors
f.closed

# 2. 
f = open("stu.txt","r")
for i in f:
    print(i)
f.close()

# 3. readlines
f = open("stu.txt","r")
fdata = f.readlines()
print(fdata)
print(type(fdata))          # <class 'list'>
print(len(fdata))
f.close()

# 4. readline
f = open("stu.txt","r")
fdata = f.readline()
print(fdata)
print(type(fdata))          # <class 'str'>
f.close()

# 5. read
f = open("stu.txt","r")
fdata = f.read(20)
print(fdata)
print(type(fdata))          # <class 'str'>
f.close()

# 6. tell & seek
f = open("stu.txt","r")
fdata = f.tell()
fdata2 = f.seek(10)
print(fdata)
print(fdata2)
print(type(fdata))          # <class 'int'>
print(type(fdata2))         # <class 'int'>
f.close()

# 7. write
f = open("stu.txt","w")
f.write("Hello \n")
f.write("Krutarth")
f.close()

# 8. append
f = open("stu.txt","a")
f.write("Roman \n")
f.write("Regins")
f.close()

# 9. binary mode
f = open("stu.txt","rb")
fdata = f.read()
print(fdata)
f.close()

# 10. comma separated values
f = open("stu.txt","r")
for i in range(2):
    fname = input("Enter the name: ")
    sal = input("Enter the salary: ")
    f.write(f"{fname},{sal}\n")
f.close()

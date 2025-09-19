f = open("num.txt","r")
line = input("Enter number:")
fdata = f.readlines()
print(f"First {line} line")
print(fdata[:line]) #first n line
print(fdata[line:]) #last n line
print(len(fdata)-line)
print(len(fdata))
f.close()


#Line count
f = open("num.txt","r")
d = f.readlines()
print("#of lines :",len(d))
n = 4
print("first",n,"lines",d[:n])
print("Last",n,"lines",d[len(d)])

#character count
f = open("num.txt","r")
data = f.read()
cnt = 0
for i in data:
    cnt += 1
    print("The characters are:",cnt)
f.close()


#Employee Dictionary
d = {0 :[1,"aaa",1000],1 : [2,"Het",5000],2:[3,"Krutarth",8900]}
tot = 0
for v in d.values():
    print(v[2])
    print(type(v[2]))
    tot=tot+v[2]
    print("Total Salary is:",tot)

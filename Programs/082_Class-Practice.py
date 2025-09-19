# 1.
od = {1:25, 2:23, 3:21}
a = sorted(od.values())
print(a)

# 2.
d1 = {1:"het",2:"krutarth"}
d2 = {4:"superman",5:"spiderman"}
d1.update(d2)
print(d1)

# 3.
print(sum(d1.values()))
print(sum(d1.keys()))

# 4.
s = 1
d1 = {1:2,2:90,3:50}
for i in d1.values():
    s = s * i
print(s)

# 5. wap get key from user and modify value
d = {1:20,2:30}
u = int(input("Enter key : "))
y = int(input("Enter value : "))
d[u] = y
print(d)

# 6. wap frequency repeat count
d ={1:20,2:30,3:40,4:20}
a = {}
for i in d.values():
    if i not in a.keys():
        a[i] = 1
    else:
        a[i] = a[i] + 1
print(a)

# 7. wap remove duplicate
d1 = {1: 10, 2: 20, 3: 20, 4: 30}
d2 = {}

for v in d1.values():
    if v not in d2.values():
        d2[v] = v

print(d2)

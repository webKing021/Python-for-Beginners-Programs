#  WAP to take User-Input empid and if the salary is less than 25,000 then increment by 1,000 else no change.
d = {1:20000, 2:25000, 3:22000, 4:27000}
e = int(input("Enter empid: "))
if e in d:
    if d[e] < 25000:
        d[e] = d[e] + 1000
    else:
        print("No Change")
print(d)

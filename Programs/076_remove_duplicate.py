# WAP to Remove Duplicate values from dict.
d = {1:1, 2:2, 3:2, 4:3}
for i in d:
    if (d[i] in d.values()):
        d.pop(i)
    else:
        print("No Duplicate Values")
print(d)

l1 = [1, 2, 3, 4, 5, 8, 4, 3]
l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)
    else:
        print(i, "is a duplicate")

print(l1)
print(l2)

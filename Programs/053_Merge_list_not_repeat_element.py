# merged list without duplicate elements in the merged list
l1 = [1, 2, 3, 4, 5]
l2 = [2, 6, 8, 5, 10]

# Method 1: Using set to remove duplicates
l3 = list(set(l1 + l2))
print("Method 1 (using set):", l3)

# Method 2: Using a loop to check for duplicates
l3 = l1.copy()
for item in l2:
    if item not in l3:
        l3.append(item)
print("Method 2 (using loop):", l3)
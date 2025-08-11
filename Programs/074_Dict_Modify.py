# i.) Add values into dict.
# ii.) Get the keys.
# iii.) Find min & max values.
# iv.) Count the number of elements in dict.

d = {1:21, 2:22, 3:20, 4:23}
print(d)

d[5] = 24
print(d)
print(d.keys())
print(min(d.values()))
print(max(d.values()))
print(len(d))


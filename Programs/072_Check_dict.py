# WAP to take User-Input & check if it is present in the dict or not
d = {1:21, 2:22, 3:20, 4:23}
key = int(input("Enter a key: "))
if key in d.keys():
    print("Key is present")
else:
    print("Key is not present")

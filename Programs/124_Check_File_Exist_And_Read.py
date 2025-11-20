#124. Check whether file exists or not and if exists then read data

import os

filename = input("Enter file name: ")

if os.path.exists(filename):
    print("File exists. Contents are:")
    with open(filename, "r") as f:
        print(f.read())
else:
    print("File does not exist.")

#125. Read a group of strings from a text file

filename = input("Enter file name: ")

with open(filename, "r") as f:
    print("Strings in file:")
    for line in f:
        print(line.rstrip("\n"))

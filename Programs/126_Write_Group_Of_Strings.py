#126. Write a group of strings in a text file

filename = input("Enter file name: ")
n = int(input("How many strings to write? "))

with open(filename, "w") as f:
    for i in range(n):
        s = input("Enter string " + str(i + 1) + ": ")
        f.write(s + "\n")

print("Strings written to", filename)

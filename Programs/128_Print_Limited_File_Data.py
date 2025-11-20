#128. Print the limited data from a file

filename = input("Enter file name: ")
n = int(input("Enter number of characters to read: "))

with open(filename, "r") as f:
    data = f.read(n)

print("First", n, "characters:")
print(data)

#123. Append data and then read data from a file

filename = input("Enter file name: ")

text_to_append = input("Enter text to append: ")
with open(filename, "a") as f:
    f.write(text_to_append + "\n")

print("Current file contents:")
with open(filename, "r") as f:
    print(f.read())

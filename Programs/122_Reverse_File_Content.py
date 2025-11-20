#122. Reverse the content of a file

infile = input("Enter source file name: ")
outfile = input("Enter destination file name: ")

with open(infile, "r") as f:
    data = f.read()

rev = data[::-1]

with open(outfile, "w") as f:
    f.write(rev)

print("Reversed content written to", outfile)

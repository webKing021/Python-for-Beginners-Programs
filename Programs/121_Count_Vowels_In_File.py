#121. Find out the number of vowels in a file

filename = input("Enter file name: ")
vowels = "aeiouAEIOU"
count = 0

with open(filename, "r") as f:
    for ch in f.read():
        if ch in vowels:
            count += 1

print("Number of vowels:", count)

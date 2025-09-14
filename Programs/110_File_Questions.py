#1.Copy content from one file to another
f1 = open("source.txt", "r")
f2 = open("copy.txt", "w")

for line in f1:
    f2.write(line)

f1.close()
f2.close()
print("File copied successfully.")

#2.Read a file line by line and store it in the list:
file = open("example.txt", "r")
lines_list = []
for line in file:
    # Remove newline character and add to list
    lines_list.append(line.strip())
file.close()
print(lines_list)

#3.Find the longest word from file
file = open("words.txt", "r")
longest_word = ""  # Variable to store the longest word
for line in file:
    words = line.split()  # Split line into words
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
file.close()
print("Longest word:", longest_word)

#4. Get the size of the file
import os
size = os.path.getsize("data.txt")
print("File size:", size, "bytes")

#5.Read two lines from file and combine 1st and 2nd line
f = open("data.txt", "r")
line1 = f.readline().strip()
line2 = f.readline().strip()
f.close()
combined = line1 + " " + line2
print("Combined line:", combined)

# String Operations - 2

# 1. Concatenation
# Definition: Join two or more strings using +.

a = "Krutarth "
b = "Python"
result = a + b
print(result)

# 2. Repetition
# Definition: Repeat a string multiple times using *.

print(a * 3)

# 3. Length
# Definition: Get the number of characters using len().
print(len(a))
print(len(b))
print(len(result))

# 4. Indexing
# Definition: Access a character at a specific position using [].
print(a[0])
print(b[1])
print(result[2])

# 5. Slicing
# Definition: Extract a substring using [start:end].
print(a[0:3])
print(b[1:4])
print(result[2:6])

# until 
print(a[0:3])
print(a[0:])
print(a[:3])
print(a[:])

# reverse
print(a[::-1])

# 6. Membership
# Definition: Check if a substring exists using in or not in.
print("Py" in "Python")
print("java" not in "Python")

# 7. Case Conversion
# upper(): Convert to uppercase.
# lower(): Convert to lowercase.
# title(): Capitalize first letter of each word.
# capitalize(): Capitalize first letter of the string.
# swapcase(): Swap case of all characters.

c = "Krutarth Python"
print(c.upper())
print(c.title())
print(c.capitalize())
print(c.swapcase())

# 8. Striping Spaces
# strip(): Removes leading and trailing spaces.
# lstrip(): Removes leading spaces.
# rstrip(): Removes trailing spaces.

a = "   krutarth   "
print(a.strip())
print(a.lstrip())
print(a.rstrip())

# 9. Replace
# Definition: Replace a substring with another.
a = "I am Batman"
print(a.replace("Batman", "Superman"))
print(a.replace("Spiderman", "Ironman", 1))      # 1 means replace only once

# 10. Split
# Definition: Split a string into a list.
a = "Batman, Superman, Ironman"
print(a.split(","))
print(a.split())
print(a.split("a"))

# 11. Join
# Definition: Join elements of a list into a string.
fruits = ['apple', 'banana', 'mango']
print(", ".join(fruits))

# 12. Find & Index
# find(): Returns the index of first occurrence, or -1 if not found.
# index(): Returns the index, or raises an error if not found.
a = "Batman loves Catwoman"
print(a.find("o"))    # 4
print(a.index("Catwoman"))  # 6

# 13. Count
# Definition: Count the occurrences of a substring.
a = "Spiderman "
print(a.count("l"))  # 3
print(a.count("o"))  # 2
print(a.count("Spiderman", 0, 10))          # 1

# 14. isdigit(), isalpha(), isalnum(), isspace()
# Definition: Check for character type.
# isdigit() → Only digits.
# isalpha() → Only alphabets.
# isalnum() → Only alphanumeric.
# isspace() → Only whitespace.
print("123".isdigit())     # True
print("abc".isalpha())     # True
print("abc123".isalnum())  # True
print("   ".isspace())     # True

# 15. rfind() / rindex()
# Definition: Like find() and index(), but searches from the right.
a = "hello world hello"
print(a.rfind("hello"))   # 12
print(a.rindex("hello"))  # 12
print(a.rfind("l", 0, 10))       # 9
print(a.rindex("l", 0, 10))      # 9

# 16. zfill(width)
# Definition: Pads the string on the left with zeros to fill a given width.
# If the width is less than or equal to the string length, the original string is returned.
print("123".zfill(5))     # 00123
print("123".zfill(2))     # 123

# 17. title()
# Definition: Converts the first character of each word to uppercase.
print("batman of gotham city".title())  # Batman Of Gotham City

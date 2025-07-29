# Program to count vowels and consonants in a string using two methods

str = "Krutarth is a good Boy"
# Method 1: Without using membership operator
vcnt = 0
ccnt = 0

for i in str:
    if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or \
        i == "A" or i == "E" or i == "I" or i == "O" or i == "U"):
        vcnt = vcnt + 1
    else:
        ccnt = ccnt + 1

print(f"Vowels: {vcnt}")
print(f"Consonants: {ccnt}")

# Method 2: Using membership operator
vcnt = 0
ccnt = 0
vowels = 'aeiouAEIOU'

for i in str:
    if (i in vowels):
        vcnt = vcnt + 1
    else:
        ccnt = ccnt + 1

print(f"Vowels: {vcnt}")            
print(f"Consonants: {ccnt}")

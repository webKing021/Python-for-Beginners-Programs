# WAP to check user-input string is Pangram or not, and also Write an Algorithem for it
# Algorithm:
# Define a function called is_pangram that takes a sentence as input.
# Inside the function: a. Convert the sentence to lowercase using the lower() method to make the comparison case-insensitive. b. Create a set named letters that stores all unique characters present in the sentence. c. Use the filter() function with a lambda function to remove any non-alphabetic characters from the letters This step ensures that only alphabet letters are considered in the pangram check. d. Compare the letters set with the set of all lowercase alphabet letters using the issubset() method. The string.ascii_lowercase constant from the string module provides all lowercase letters of the alphabet. e. Return True if the letters set contains all the lowercase alphabet letters, indicating that the sentence is a pangram. Otherwise, return False.
# After defining the is_pangram function, the program then tests the function by taking input from the user and displaying whether the input sentence is a pangram or not.

# Code:
s = "The quick brown fox jumps over the lazy dog"

# Function to check if a sentence is a pangram
def is_pangram(sentence):
    # Convert the sentence to lowercase
    sentence = sentence.lower()
    
    # Create a set of unique letters in the sentence
    letters = set(filter(str.isalpha, sentence))
    
    # Check if the set of letters contains all lowercase alphabet letters
    return letters.issubset(string.ascii_lowercase)

# Test the function
user_input = input("Enter a sentence: ")
if is_pangram(user_input):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")

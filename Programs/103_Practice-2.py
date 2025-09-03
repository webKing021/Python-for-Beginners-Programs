# practice-2

# 1. WAP function to find the maximum of three numbers.
def max_of_three(a, b, c):
    if a > b:
        print(a)
    elif b > c:
        print(b)
    else:
        print(c)

max_of_three(12, 21, 31)

# 2. Sum all numbers in the list.
def sum_list(nums):
    total = 0
    for x in nums:
        total = total + x
    return total

l1 = [1, 2, 3, 4, 5]
print(sum_list(l1))

# 3. Multiply all numbers in a list.
def multiply_list(nums):
    total = 1
    for x in nums:
        total = total * x
    return total

l2 = [1, 2, 3, 4, 5]
print(multiply_list(l2))


# 4. WAP to reverse a string.
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))

# 5. WAP Function to check whether a number falls within a given range.
def check_range(num, start, end):
    if num >= start and num <= end:
        return True
    else:
        return False

print(check_range(10, 1, 10))

# 6. WAP Function that takes a list and returns a new list with distinct elements from the first list.
def distinct_list(nums):
    return list(set(nums))

l3 = [1, 2, 2, 3, 4, 4, 5]
print(distinct_list(l3))

# 7. WAP to print the even numbers from a given list.
def even_list(nums):
    for num in nums:
        if num % 2 == 0:
            print(num)

l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list(l4)

# 8. WAP to Sort Hyphen-Separated Sequence of Words Alphabetically.
def sort(s):
    words = s.split("-")
    words.sort()
    return "-".join(words)

print(sort("green-red-yellow-black-white"))

# 9. WAP function to create and print a list where the values are the squares of numbers b/w 1 and 30 (both included).
def square_list(nums):
    return [x * x for x in nums]

l5 = range(1, 31)
print(square_list(l5))


# 10.  WAP Function that takes a number as a parameter and checks whether the number is prime or not.
def prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False

print(prime(10))


# 11. WAP function to calculate the factorial of a number, (a non-negative int). The function accepts the number as an argument.
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(5))


# 12. WAP function that checks whether a passed string is a palindrome or not.
def palindrome(s):
    return s == s[::-1]

print(palindrome("madam"))

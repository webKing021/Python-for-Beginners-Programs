# <img src="Programs/Python-Light.svg" width="32" height="32"> Python Programming Notes By Krutarth Raychura

✨ Concise explanations and definitions of Python concepts for quick exam reference. 🚀

> 💡 **Study Tip**: These notes cover essential Python concepts with clear examples for efficient exam preparation!

## 📋 Table of Contents
1. 📤 [Basic Output](#-basic-output)
2. 🔠 [Variables and Data Types](#-variables-and-data-types)
3. ⌨️ [User Input](#-user-input)
4. 🧮 [Basic Operators](#-basic-operators)
5. 🔄 [Control Flow](#-control-flow)
   - 🔁 [For Loop](#-for-loop)
   - 🔀 [While Loop](#-while-loop)
   - 🔄 [Loop Control Statements](#-loop-control-statements)
6. 🔀 [Conditional Statements](#-conditional-statements)
7. 📝 [String Formatting](#-string-formatting)
8. 🔄 [Number Conversions](#-number-conversions)
9. 🧰 [String Functions](#-string-functions)
10. 📋 [Menu-Driven Programming](#-menu-driven-programming)
11. 🔄 [Loop Exercise Programs](#-loop-exercise-programs)
12. 📋 [List Operations](#-list-operations)
---

## 📤 Basic Output

### 🖨️ Print Function
**Definition**: The `print()` function displays output to the console.

```python
print("Hello World!")  # Outputs: Hello World!
```

---

## 🔠 Variables and Data Types

### 📦 Variables
**Definition**: Variables are containers for storing data values.

```python
x = 21        # Integer variable
name = "Krutarth"  # String variable
```

### 🏷️ Data Types
**Definition**: Data types categorize the type of data a variable can hold.

#### 📊 Common Data Types:
- 🔢 **int**: Integer values (e.g., 5, -3, 42)
- 🔣 **float**: Decimal values (e.g., 3.14, -0.001, 2.0)
- 📝 **str**: Text strings (e.g., "Hello", 'Python')
- 📋 **list**: Ordered collection of items (e.g., [1, 2, 3])
- 📦 **tuple**: Ordered, immutable collection (e.g., (1, 2, 3))
- 🔑 **dict**: Dictionary with key-value pairs (e.g., {'key': 'value'})
- 🧩 **set**: Collection of unique items (e.g., {1, 2, 3})
- ✅ **bool**: Boolean values (True or False)
- ❓ **None**: Represents the absence of a value


```python
x = 10
print(type(x))  # Outputs: <class 'int'>

y = 10.21
print(type(y))  # Outputs: <class 'float'>

z = "Krutarth"
print(type(z))  # Outputs: <class 'str'>
```

---

## ⌨️ User Input

### 📥 Input Function
**Definition**: The `input()` function allows the program to receive input from the user.

```python
user = input("Enter your name: ")
print("Hello", user, "!")
```

### 🔄 Type Conversion
**Definition**: Converting input data from one type to another.

```python
x = int(input("Enter a number: "))  # Converts input string to integer
y = float(input("Enter a number: "))  # Converts input string to float
z = str(input("Enter a number: "))  # Converts input string to string

print(type(x))  # Outputs: <class 'int'>
print(type(y))  # Outputs: <class 'float'>
print(type(z))  # Outputs: <class 'str'>

```

---

## 🧮 Basic Operators

### 1.🔢 Python Arithmetic Operators
**Definition**: Operators used to perform mathematical operations. which contain 1 operator and 2 operands.

| Operator | Name           | Description                                | Example  | Result |
| -------- | -------------- | ------------------------------------------ | -------- | ------ |
| `+`      | Addition       | Adds two numbers                           | `5 + 2`  | `7`    |
| `-`      | Subtraction    | Subtracts second number from first         | `5 - 2`  | `3`    |
| `*`      | Multiplication | Multiplies two numbers                     | `5 * 2`  | `10`   |
| `/`      | Division       | Divides first number by second             | `5 / 2`  | `2.5`  |
| `//`     | Floor Division | Division that rounds down to nearest int   | `5 // 2` | `2`    |
| `%`      | Modulus        | Returns the remainder                      | `5 % 2`  | `1`    |
| `**`     | Exponentiation | Raises first number to the power of second | `5 ** 2` | `25`   |

### Example Code:

```python
# Addition
print(10 + 4)      # 14

# Subtraction
print(10 - 4)      # 6

# Multiplication
print(10 * 4)      # 40

# Division
print(10 / 4)      # 2.5

# Floor Division
print(10 // 4)     # 2

# Modulus
print(10 % 4)      # 2

# Exponentiation
print(2 ** 4)      # 16

# Unary operators
x = 5
print(-x)          # -5
print(+x)          # 5
```

### 2.✍️ Assignment (Short Hand) Operators
**Definition**: Operators that perform a mathematical operation and assign the result to a variable.

| Operator | Name           | Description                                | Example  | Result |
| -------- | -------------- | ------------------------------------------ | -------- | ------ |
| `=`      | Assignment     | Assigns value to variable                  | `x = 5`  | `5`    |
| `+=`     | Addition       | Adds and assigns                           | `x += 2` | `7`    |
| `-=`     | Subtraction    | Subtracts and assigns                      | `x -= 2` | `3`    |
| `*=`     | Multiplication | Multiplies and assigns                     | `x *= 2` | `10`   |
| `/=`     | Division       | Divides and assigns                        | `x /= 2` | `2.5`  |
| `//=`    | Floor Division | Floor divides and assigns                  | `x //= 2`| `2`    |
| `%=`     | Modulus        | Modulus and assigns                        | `x %= 2` | `1`    |
| `**=`    | Exponentiation | Exponentiates and assigns                  | `x **= 2`| `25`   |


```python
x = 12
y = 15
x += y
print(x)  # 27
x = 12    # Reset x
x -= y
print(x)  # -3
x = 12    # Reset x
x *= y
print(x)  # 180
x = 12    # Reset x
x /= y
print(x)  # 0.8
x = 12    # Reset x
x //= y
print(x)  # 0
x = 12    # Reset x
x %= y
print(x)  # 12
x = 12    # Reset x
x **= y
print(x)  # Very large number
```

### 3.⚖️ Comparison (Relational) Operators
**Definition**: Operators that compare two values and return a boolean result.

| Operator | Description      | Example  |
| -------- | ---------------- | -------- |
| `==`     | Equal to         | `a == b` |
| `!=`     | Not equal to     | `a != b` |
| `>`      | Greater than     | `a > b`  |
| `<`      | Less than        | `a < b`  |
| `>=`     | Greater or equal | `a >= b` |
| `<=`     | Less or equal    | `a <= b` |


### Example Code:

```python
# Equal
print(10 == 4)      # False

# Not Equal
print(10 != 4)      # True

# Greater Than
print(10 > 4)       # True

# Less Than
print(10 < 4)       # False

# Greater or Equal
print(10 >= 4)      # True

# Less or Equal
print(10 <= 4)      # False

```

### 4.🧠 Logical Operators

**Definition**: Operators that combine multiple conditions.

| Operator | Description      | Example  |
| -------- | ---------------- | -------- |
| `and`    | Logical AND      | `a and b` |
| `or`     | Logical OR       | `a or b`  |
| `not`    | Logical NOT      | `not a`   |


### Example Code:

```python
# Logical AND
print(10 > 4 and 10 < 20)  # True

# Logical OR
print(10 > 4 or 10 < 20)   # True

# Logical NOT
print(not 10 > 4)           # False
```



### 5.🧱 Bitwise Operators
**Definition**: Operators that perform bitwise operations on integers.

| Operator | Description         | Example  |
| -------- | ------------------- | -------- |
| `&`      | Bitwise AND         | `a & b`  |
| `|`     | Bitwise OR          | `a \| b`  |
| `^`      | Bitwise XOR         | `a ^ b`  |
| `~`      | Bitwise NOT         | `~a`     |
| `<<`     | Bitwise Left Shift  | `a << 2` |
| `>>`     | Bitwise Right Shift | `a >> 2` |

### Example Code:

```python
# Bitwise AND
print(10 & 4)  # 4

# Bitwise OR
print(10 | 4)  # 14

# Bitwise XOR
print(10 ^ 4)  # 12

# Bitwise NOT
print(~10)  # -11

# Bitwise Left Shift
print(10 << 2)  # 40

# Bitwise Right Shift
print(10 >> 2)  # 2
```

### 6.🧩 Unary Operators
**Definition**: Operators that work on a single operand.

| Operator | Description         | Example  |
| -------- | ------------------- | -------- |
| `+`      | Positive            | `+a`     |
| `-`      | Negative            | `-a`     |
| `~`      | Bitwise NOT         | `~a`     |

### Example Code:

```python
# Positive
print(+10)  # 10

# Negative
print(-10)  # -10

# Bitwise NOT
print(~10)  # -11
```

### 7.🧪 Ternary Operator
**Definition**: A shorthand way to write simple if-else statements.

Syntax:
```
value = true_value if condition else false_value
```

```python
# Simple if-else statement
x = 10
result = "Positive" if x > 0 else "Negative"
print(result)  # Outputs: Positive

# Nested ternary operator
x = 10
result = "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(result)  # Outputs: Positive
```


---

## 🔄 Control Flow

### 🔁 For Loop
**Definition**: A loop that iterates over a sequence (like a list, tuple, or string) or range.

Syntax :
```
for item in sequence:
    # Do something with item
```

```python
# Loop from 0 to 3
for i in range(4):
    print(i)  # Outputs: 0, 1, 2, 3

# Loop from 50 to 20 with step -10
for i in range(50, 10, -10):
    print(i)  # Outputs: 50, 40, 30, 20

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with index using enumerate
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
```

#### 🔄 For Loop with Else
**Definition**: A for loop can have an optional else block that executes when the loop completes normally (without a break statement).

```python
# Simple for loop with else
for i in range(1, 10):
    print(i)
else:
    print("for loop is over")  # This executes after printing numbers 1-9

# With break statement (else block won't execute)
for i in range(1, 10):
    if i == 5:
        break
    print(i)
else:
    print("This won't be printed")  # This won't execute because of the break
```

**Key Points about Loop with Else**:
- The else block executes only if the loop completes all iterations normally
- If a break statement is encountered, the else block is skipped
- This feature is unique to Python and can be used for implementing search algorithms where you need to know if the search was successful or not

#### 🔄 Nested For Loops
**Definition**: A for loop inside another for loop.

```python
# Print a pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Output:
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
```

### 🔀 While Loop
**Definition**: A loop that executes as long as a condition is true.

Syntax :
```
while condition:
    # Do something
```

```python
# Count from 0 to 3
i = 0
while i < 4:
    print(i)  # Outputs: 0, 1, 2, 3
    i += 1

# Infinite loop with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == "quit":
        break
    print("You entered:", user_input)
```

#### 🔄 While Loop with Else
**Definition**: Similar to for loops, while loops can also have an else block that executes when the loop condition becomes false (when the loop completes normally without a break statement).

```python
# While loop with else example
cnt = 1
while(cnt <= 10):
    print(cnt)
    cnt = cnt + 1
else:
    print("while loop is over")  # This executes when cnt becomes 11
```

### 🔄 Loop Control Statements

#### ⏹️ Break Statement
**Definition**: Terminates the loop and transfers execution to the statement immediately following the loop. Any code after the break statement in the loop is not executed.

```python
# Example of break statement
for i in range(2, 10):
    if i % 2 == 0:
        print(f"{i} is even number")
        break  # Exit loop after finding first even number
        # This line is never executed
        num = 3
print(i)  # Outputs: 2 (the value where the loop was broken)
```

#### ⏭️ Continue Statement
**Definition**: Skips the rest of the code inside the loop for the current iteration and continues with the next iteration. Code after the continue statement in the current iteration is not executed.

```python
# Example of continue statement
for i in range(2, 10):
    if i % 2 == 0:  # For even numbers
        print(f"{i} is even number")
        continue  # Skip to next iteration
        # This line is never executed
        num = 3
print(i)  # Outputs: 9 (the last value in the range)
```

#### 🔄 Pass Statement
**Definition**: A null statement that does nothing. It's used as a placeholder when a statement is required syntactically but no action is needed. Unlike break and continue, code after pass is executed normally.

```python
for i in range(5):
    if i == 2:
        # TODO: Add code later
        pass
    print(i)  # Outputs: 0, 1, 2, 3, 4
```
---

## 🔀 Conditional Statements

### 🔁 If Statement
**Definition**: A statement that executes if a condition is true.

Syntax :
```
if condition:
    # Do something
```

```python
# Simple if statement
x = 10
if x > 0:
    print("x is positive")
```

### 🔁 If-Else Statement
**Definition**: A statement that executes if a condition is true, and another statement if it's false.

Syntax :
```
if condition:
    # Do something
else:
    # Do something else
```

```python
# Simple if-else statement
x = 10
if x > 0:
    print("x is positive")
else:
    print("x is negative")
```

### 🔁 If-Elif-Else Statement
**Definition**: A statement that executes if a condition is true, and another statement if it's false.

Syntax :
```
if condition:
    # Do something
elif condition:
    # Do something else
else:
    # Do something else
```

```python
# Simple if-else statement
x = 10
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
```

### 🔁 Nested If Statements
**Definition**: A statement that executes if a condition is true, and another statement if it's false.

Syntax :
```
if condition:
    # Do something
    if condition:
        # Do something else
    else:
        # Do something else
else:
    # Do something else
```

```python
# Nested if statement
x = 10
if x > 0:
    print("x is positive")
    if x > 10:
        print("x is greater than 10")
    else:
        print("x is less than 10")
else:
    print("x is negative")
```

## 📝 String Formatting

### 🔤 Formatted Strings using % Operator
**Definition**: A way to format strings using the % operator, similar to printf in C.

```python
print("Name: %s, Age: %d" % ("Krutarth", 20))  # Outputs: Name: Krutarth, Age: 20

print("%5.2f" % (3.1415926))  # Outputs:  3.14
```

### 🔠 F-Strings (Formatted String Literals)
**Definition**: A concise way to embed expressions inside string literals using curly braces {}.

```python
name = "Krutarth"
age = 20
print(f"Name: {name}, Age: {age}")  # Outputs: Name: Krutarth, Age: 20
print(f"Value of pi: {3.1415926:.2f}")  # Outputs: Value of pi: 3.14
```

## 🔄 Number Conversions

### 🔢 Number Base Conversions
**Definition**: Converting numbers between different bases (decimal, binary, octal, hexadecimal).

```python
# Decimal to other bases
decimal_num = 42
print(bin(decimal_num))  # Outputs: 0b101010 (binary)
print(oct(decimal_num))  # Outputs: 0o52 (octal)
print(hex(decimal_num))  # Outputs: 0x2a (hexadecimal)

# Other bases to decimal
print(int('101010', 2))  # Outputs: 42 (binary to decimal)
print(int('52', 8))      # Outputs: 42 (octal to decimal)
print(int('2a', 16))     # Outputs: 42 (hexadecimal to decimal)
```

### 🔤 Character and ASCII Conversions
**Definition**: Converting between characters and their ASCII/Unicode values.

```python
# Character to ASCII value
print(ord('A'))  # Outputs: 65

# ASCII value to character
print(chr(65))   # Outputs: A
```

## 🧰 String Functions

### 📝 str() Function
**Definition**: Converts an object to its string representation.

```python
num = 42
print(str(num))  # Outputs: "42"
```

### 🔍 eval() Function
**Definition**: Evaluates a string as a Python expression.

```python
print(eval('2 + 3 * 4'))  # Outputs: 14
x = 10
print(eval('x * 2'))      # Outputs: 20
```

### 📋 repr() Function
**Definition**: Returns a string containing a printable representation of an object.

```python
s = 'Hello\nWorld'
print(repr(s))  # Outputs: 'Hello\nWorld'
```

## 📋 Menu-Driven Programming
**Definition**: A programming approach where users are presented with a menu of options to choose from, and the program executes different actions based on their selection.

### 🔢 Basic Menu Structure
**Definition**: The fundamental structure of a menu-driven program includes displaying options, getting user input, and executing code based on that input.

```python
# Basic menu structure
ch = 9  # Initialize with a value that won't exit immediately
while(ch != 3):  # Loop until exit option is selected
    print("**** Menu ****")
    print("1. Option One")
    print("2. Option Two")
    print("3. Exit")
    
    ch = int(input("Enter your choice: "))  # Get user choice
    
    if(ch == 1):
        # Code for option 1
        print("You selected Option One")
    elif(ch == 2):
        # Code for option 2
        print("You selected Option Two")
    elif(ch == 3):
        print("Exiting program...")
    else:
        print("Invalid choice! Please try again.")
```

### 💡 Tips for Menu-Driven Programs
- Always include an exit option to terminate the program
- Validate user input to handle unexpected entries
- Use clear and descriptive menu options
- Consider using a loop to return to the menu after each operation
- Add error handling for operations that might fail (like division by zero)

## 🔄 Loop Exercise Programs

Here are some practical loop exercise programs to practice Python loops:

1. **Print Natural Numbers**: Using while loop to print first 10 natural numbers.
   ```python
   i = 1
   while i <= 10:
       print(i)
       i += 1
   ```

2. **Pattern Printing**: Using nested loops to print patterns.
   ```python
   rows = 5
   for i in range(1, rows + 1):
       for j in range(1, i + 1):
           print("*", end=" ")
       print()
   ```

3. **Sum of Numbers**: Calculate sum of all numbers from 1 to n.
   ```python
   n = 10
   sum = 0
   for i in range(1, n + 1):
       sum += i
   print(f"Sum: {sum}")  # Outputs: Sum: 55
   ```

4. **Multiplication Table**: Print multiplication table of a given number.
   ```python
   num = 5
   for i in range(1, 11):
       print(f"{num} x {i} = {num * i}")
   ```

5. **Count Digits**: Count the total number of digits in a number.
   ```python
   num = 12345
   count = len(str(num))
   print(f"Number of digits: {count}")  # Outputs: Number of digits: 5
   ```

6. **Reverse List**: Print list in reverse order using a loop.
   ```python
   my_list = [1, 2, 3, 4, 5]
   for i in range(len(my_list) - 1, -1, -1):
       print(my_list[i])
   ```

7. **Prime Numbers**: Display all prime numbers within a range.
   ```python
   start, end = 10, 20
   for num in range(start, end + 1):
       if num > 1:
           for i in range(2, int(num**0.5) + 1):
               if num % i == 0:
                   break
           else:
               print(num, end=" ")
   ```

8. **Fibonacci Series**: Display Fibonacci series up to n terms.
   ```python
   n = 10
   a, b = 0, 1
   print(a, b, end=" ")
   for i in range(2, n):
       c = a + b
       print(c, end=" ")
       a, b = b, c
   ```

9. **Factorial**: Find the factorial of a given number.
   ```python
   num = 5
   fact = 1
   for i in range(1, num + 1):
       fact *= i
   print(f"{num}! = {fact}")  # Outputs: 5! = 120
   ```

10. **Reverse Integer**: Reverse a given integer number.
    ```python
    num = 12345
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    print(f"Reversed number: {reversed_num}")  # Outputs: Reversed number: 54321
    ```

## 📋 List Operations

### 📝 List Methods
**Definition**: Python lists have built-in methods for adding, removing, and manipulating elements.

```python
# Common List Methods
my_list = [1, 2, 3, 4, 5]

# Adding elements
my_list.append(6)        # Adds element to the end: [1, 2, 3, 4, 5, 6]
my_list.insert(0, 0)     # Inserts element at index: [0, 1, 2, 3, 4, 5, 6]
my_list.extend([7, 8])   # Adds multiple elements: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Removing elements
my_list.remove(0)        # Removes first occurrence of value: [1, 2, 3, 4, 5, 6, 7, 8]
popped = my_list.pop()   # Removes and returns last element: 8, list becomes [1, 2, 3, 4, 5, 6, 7]
popped = my_list.pop(0)  # Removes element at index: 1, list becomes [2, 3, 4, 5, 6, 7]

# Other operations
len(my_list)             # Returns length of list: 6
my_list.count(3)         # Counts occurrences of element: 1
my_list.index(5)         # Returns index of first occurrence: 3
my_list.sort()           # Sorts list in-place: [2, 3, 4, 5, 6, 7]
my_list.reverse()        # Reverses list in-place: [7, 6, 5, 4, 3, 2]
```

### 📚 Stack Implementation
**Definition**: A stack is a Last-In-First-Out (LIFO) data structure that can be implemented using a Python list.

```python
# Stack implementation using a list
stack = []

# Push operation (add to top)
stack.append(1)    # [1]
stack.append(2)    # [1, 2]
stack.append(3)    # [1, 2, 3]

# Pop operation (remove from top)
top_item = stack.pop()  # Returns 3, stack becomes [1, 2]
top_item = stack.pop()  # Returns 2, stack becomes [1]

# Check if stack is empty
is_empty = len(stack) == 0  # False
```

### 🔄 Queue Implementation
**Definition**: A queue is a First-In-First-Out (FIFO) data structure that can be implemented using a Python list.

```python
# Queue implementation using a list
queue = []

# Enqueue operation (add to end)
queue.append(1)    # [1]
queue.append(2)    # [1, 2]
queue.append(3)    # [1, 2, 3]

# Dequeue operation (remove from front)
front_item = queue.pop(0)  # Returns 1, queue becomes [2, 3]
front_item = queue.pop(0)  # Returns 2, queue becomes [3]

# Check if queue is empty
is_empty = len(queue) == 0  # False
```

### 🔍 List Manipulation

#### Finding Duplicates
**Definition**: Identifying and handling duplicate elements in a list.

```python
# Finding duplicates in a list
original_list = [1, 2, 3, 4, 5, 3, 2, 7]
unique_list = []
duplicates = []

for item in original_list:
    if item not in unique_list:
        unique_list.append(item)
    else:
        duplicates.append(item)

print(f"Original list: {original_list}")  # [1, 2, 3, 4, 5, 3, 2, 7]
print(f"Unique elements: {unique_list}")  # [1, 2, 3, 4, 5, 7]
print(f"Duplicates: {duplicates}")        # [3, 2]
```

#### Merging Lists Without Duplicates
**Definition**: Combining two lists while ensuring no duplicate elements in the result.

```python
# Method 1: Using sets
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
merged_list = list(set(list1 + list2))
print(f"Merged list (using set): {merged_list}")  # [1, 2, 3, 4, 5, 6, 7, 8]

# Method 2: Using a loop
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
merged_list = list1.copy()

for item in list2:
    if item not in merged_list:
        merged_list.append(item)

print(f"Merged list (using loop): {merged_list}")  # [1, 2, 3, 4, 5, 6, 7, 8]
```

<div align="center">

### 🐍 Happy Python Coding! 🐍

*"The only way to learn a programming language is by writing programs in it." - Dennis Ritchie*

</div>
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
13. 📝 [String Operations](#-string-operations)
14. 🔤 [Vowels and Consonants](#-vowels-and-consonants)
15. 🧵 [String Immutability](#-string-immutability)
16. 📋 [List Comprehensions](#-list-comprehensions)
17. 🗑️ [Del Statement and Copy Operations](#-del-statement-and-copy-operations)
18. 📦 [Tuple Operations](#-tuple-operations)
19. 🧰 [Dictionary Essentials](#-dictionary-essentials)
20. 📋 [List Quick Patterns](#-list-quick-patterns)
21. 💾 [File Handling](#-file-handling)
22. ⚠️ [Exception Handling](#-exception-handling)
23. 🧭 [Assertions](#-assertions)
24. 🔧 [Functions](#-functions)
25. 🧾 [Docstrings](#-docstrings)
26. ⭐ [Arbitrary Positional Arguments](#-arbitrary-positional-arguments)
27. 🔁 [Recursion](#-recursion)
28. 🔄 [Call by Value vs Reference (Python)](#-call-by-value-vs-reference-python)
29. 🎯 [Advanced Function Concepts](#-advanced-function-concepts)
30. 🎨 [Decorators](#-decorators)
31. 🔄 [Generators](#-generators)
32. 📦 [Modules and Imports](#-modules-and-imports)
33. 🧮 [Built-in Math Functions](#-built-in-math-functions)
34. 🔤 [String Module](#-string-module)
35. 🎲 [Random Module](#-random-module)
36. 🔐 [Password Generation](#-password-generation)
37. 📐 [Pascal's Triangle](#-pascals-triangle)
38. 🔤 [Pangram Algorithm](#-pangram-algorithm)
39. 🧠 [Common Algorithms](#-common-algorithms)
40. 📁 [Advanced File Handling](#-advanced-file-handling)
41. 📋 [File CRUD Operations](#-file-crud-operations)
42. 🔢 [Binary File Operations](#-binary-file-operations)
43. 🎯 [Variable Scoping](#-variable-scoping)
44. 📝 [Advanced File Methods](#-advanced-file-methods)
45. 📊 [File Analysis Operations](#-file-analysis-operations)
46. 🔧 [File Utility Functions](#-file-utility-functions)
47. 🏛️ [Object-Oriented Programming (OOP)](#-object-oriented-programming-oop)
48. 🎓 [Classes and Objects](#-classes-and-objects)
49. 🔧 [Class Methods and Attributes](#-class-methods-and-attributes)
50. 🏗️ [Constructors and self](#-constructors-and-self)
51. 🧬 [Inheritance](#-inheritance)
52. 🔀 [Polymorphism](#-polymorphism)
53. 🔒 [Encapsulation](#-encapsulation)
54. 🎭 [Abstraction](#-abstraction)
55. ⚙️ [Operator Overloading](#-operator-overloading)
56. 🔄 [Method Overloading and Overriding](#-method-overloading-and-overriding)

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
---

## 📝 String Operations

### 📊 String Basics
**Definition**: Strings are sequences of characters enclosed in quotes (single, double, or triple quotes).

```python
s1 = "python"      # Double quotes
s2 = 'python'      # Single quotes
s3 = """python"""  # Triple quotes
empty_str = ""    # Empty string
```

### 📏 String Length
**Definition**: The `len()` function returns the number of characters in a string.

```python
s = "python"
print(len(s))  # Outputs: 6
```

### 🔍 Accessing Characters
**Definition**: Characters in a string can be accessed using indexing (starting from 0).

```python
s = "python"
print(s[0])  # Outputs: p (first character)
print(s[3])  # Outputs: h (fourth character)
```

### 🔪 String Slicing
**Definition**: Extracting a portion of a string using a range of indices with format `[start:end]` (end index is exclusive).

```python
s = "python"
print(s[0:2])   # Outputs: py (characters from index 0 to 1)
print(s[0:])    # Outputs: python (all characters from index 0)
print(s[:3])    # Outputs: pyt (characters from start to index 2)
print(s[:])     # Outputs: python (all characters)
print(s[::-1])  # Outputs: nohtyp (reversed string)
```

### 🔗 String Concatenation
**Definition**: Joining two or more strings together using the `+` operator.

```python
s1 = "python"
s2 = " programming"
print(s1 + s2)  # Outputs: python programming
```

### 🔄 String Repetition
**Definition**: Repeating a string multiple times using the `*` operator.

```python
s = "python"
print(s * 3)  # Outputs: pythonpythonpython
```

### 🔍 Membership Operators
**Definition**: Checking if a character or substring exists in a string using `in` and `not in` operators.

```python
s = "python"
print("y" in s)       # Outputs: True
print("z" not in s)   # Outputs: True
print("Py" in s)      # Outputs: False (case-sensitive)
```

### 🔪 String Split
**Definition**: Dividing a string into a list of substrings based on a delimiter using the `split()` method.

```python
# With specified delimiter
s1 = "apple,banana,orange"
print(s1.split(","))  # Outputs: ['apple', 'banana', 'orange']

# Without delimiter (splits by whitespace)
s2 = "apple banana orange"
print(s2.split())     # Outputs: ['apple', 'banana', 'orange']

# Split by character
s3 = "Batman, Superman, Ironman"
print(s3.split("a"))  # Outputs: ['B', 'tm', 'n, Superm', 'n, Ironm', 'n']
```

### 🔢 String Count
**Definition**: Counting occurrences of a substring in a string using the `count()` method.

```python
s = "python programming is fun, python is easy"
print(s.count("python"))  # Outputs: 2

# Count with range
s = "Spiderman"
print(s.count("Spiderman", 0, 10))  # Outputs: 1 (count in range 0-9)

# Count individual characters
s = "krutarth is good"
print(s.count("a"))  # Outputs: 1
print(s.count("i"))  # Outputs: 1
```

### 🔠 Case Conversion
**Definition**: Methods to change the case of strings.

```python
s = "Krutarth Python"
print(s.upper())       # Outputs: KRUTARTH PYTHON
print(s.lower())       # Outputs: krutarth python
print(s.title())       # Outputs: Krutarth Python
print(s.capitalize())  # Outputs: Krutarth python
print(s.swapcase())    # Outputs: kRUTARTH pYTHON
```

### 🧹 Stripping Spaces
**Definition**: Methods to remove leading and trailing whitespace.

```python
s = "   krutarth   "
print(s.strip())    # Outputs: "krutarth"
print(s.lstrip())   # Outputs: "krutarth   "
print(s.rstrip())   # Outputs: "   krutarth"
```

### 🔄 Replace
**Definition**: Replace occurrences of a substring with another using the `replace()` method.

```python
s = "I am Batman"
print(s.replace("Batman", "Superman"))  # Outputs: I am Superman

# Replace with count
print(s.replace("a", "e", 1))  # Outputs: I em Batman (only first 'a' replaced)
```

### 🔗 Join
**Definition**: Join elements of an iterable (like list) into a string using a specified delimiter.

```python
fruits = ['apple', 'banana', 'mango']
print(", ".join(fruits))  # Outputs: apple, banana, mango
```

### 🔍 Find and Index
**Definition**: Methods to find the position of a substring in a string.

```python
s = "Batman loves Catwoman"

# find() - returns index or -1 if not found
print(s.find("o"))        # Outputs: 10
print(s.find("xyz"))      # Outputs: -1

# index() - returns index or raises ValueError if not found
print(s.index("Catwoman"))  # Outputs: 13

# rfind() and rindex() - search from right to left
s = "hello world hello"
print(s.rfind("hello"))    # Outputs: 12
print(s.rindex("hello"))   # Outputs: 12
```

### 🔤 Character Type Checking
**Definition**: Methods to check the type of characters in a string.

```python
print("123".isdigit())      # Outputs: True (only digits)
print("abc".isalpha())      # Outputs: True (only alphabets)
print("abc123".isalnum())   # Outputs: True (only alphanumeric)
print("   ".isspace())      # Outputs: True (only whitespace)
```

### 0️⃣ Zero Fill
**Definition**: Pad a string with zeros on the left using the `zfill()` method.

```python
print("123".zfill(5))  # Outputs: 00123
print("123".zfill(2))  # Outputs: 123 (width less than string length)
```

---

## 🔤 Vowels and Consonants

### 📊 Counting Vowels and Consonants
**Definition**: Identifying and counting vowels (a, e, i, o, u) and consonants in a string.

#### Method 1: Without Membership Operator
```python
str = "Hello World"
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
```

#### Method 2: With Membership Operator
```python
str = "Hello World"
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
```

---

## 🧵 String Immutability

**Definition**: In Python, strings are immutable, which means once a string is created, its contents cannot be changed.

### 📝 Immutability Demonstration

```python
# Attempting to change a character in a string
s = "Hello"
try:
    s[0] = "h"  # This will raise an error
except TypeError as e:
    print(f"Error: {e}")  # Outputs: Error: 'str' object does not support item assignment

# Creating a new string is the correct way
s = "Hello"
new_s = "h" + s[1:]  # Creates a new string
print(new_s)  # Outputs: hello
```

### 📚 Multiline Strings

```python
# Using triple quotes for multiline strings
multiline_str = """This is a multiline string.
It can span multiple lines.
Very useful for documentation."""
print(multiline_str)
```

---

## 📋 List Comprehensions

**Definition**: List comprehensions provide a concise way to create lists based on existing lists or other iterables.

### 🔄 Basic Syntax

```python
# Basic syntax: [expression for item in iterable if condition]
```

### 📊 Examples

```python
# Square numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)  # Outputs: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Filter even numbers
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)  # Outputs: [2, 4, 6, 8, 10]

# Transpose a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)  # Outputs: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

---

## 🗑️ Del Statement and Copy Operations

### 🗑️ Del Statement

**Definition**: The `del` statement is used to delete objects in Python, including list elements, entire lists, variables, etc.

```python
# Delete an element from a list
my_list = [1, 2, 3, 4, 5]
del my_list[2]  # Deletes the element at index 2
print(my_list)  # Outputs: [1, 2, 4, 5]

# Delete a slice from a list
my_list = [1, 2, 3, 4, 5]
del my_list[1:3]  # Deletes elements at index 1 and 2
print(my_list)  # Outputs: [1, 4, 5]

# Delete the entire list
my_list = [1, 2, 3, 4, 5]
del my_list
# print(my_list)  # This would raise a NameError as my_list no longer exists
```

### 📋 Copy Operations

**Definition**: In Python, there are multiple ways to copy or clone a list.

#### 🔄 Shallow Copy Methods

```python
# Using the copy() method
original = [1, 2, [3, 4]]
shallow_copy1 = original.copy()

# Using slice operator
shallow_copy2 = original[:]

# Using the list() function
shallow_copy3 = list(original)

# Using the extend() method
shallow_copy4 = []
shallow_copy4.extend(original)
```

#### 🔍 Deep Copy

```python
import copy

original = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(original)

# Modifying the nested list in the original won't affect the deep copy
original[2][0] = 'X'
print(original)    # Outputs: [1, 2, ['X', 4]]
print(deep_copy)   # Outputs: [1, 2, [3, 4]]
```

#### 📊 Shallow vs Deep Copy Comparison

| Feature | Shallow Copy | Deep Copy |
|---------|-------------|----------|
| Nested Objects | References the same objects | Creates new copies of nested objects |
| Memory Usage | Less memory | More memory |
| Speed | Faster | Slower |
| Use Case | When nested objects don't need independent copies | When complete independence is required |

---

## 📦 Tuple Operations

**Definition**: Tuples are ordered, immutable collections (cannot be changed after creation). They are created using parentheses `()` and are useful for storing heterogeneous data.

### 🔹 Creating Tuples
```python
empty_tuple = ()
singleton = ("Krutarth",)  # Note the trailing comma
mixed = (21, "Krutarth", 9.29)
nested = ("Krutarth", [1, 2, 3], (4, 5, 6))
```

### 🔄 Tuple Unpacking
```python
t = (1, 2, 3)
a, b, c = t
print(a, b, c)  # Outputs: 1 2 3
```

### 🛠️ Tuple CRUD Example (from `065_Tuple_CURD.py`)
```python
t = (1, 2, 3, 4, 5)
# Add element 99 at index 2
t = t[:2] + (99,) + t[2:]
print(t)  # (1, 2, 99, 3, 4, 5)
# Delete element at index 3
t = t[:3] + t[4:]
print(t)  # (1, 2, 99, 4, 5)
# Update element at index 1 to 42
t = t[:1] + (42,) + t[2:]
print(t)  # (1, 42, 99, 4, 5)
```

💡 **Immutability Reminder**: Any "modification" of a tuple actually creates a new tuple; the original remains unchanged.

---

## 🧰 Dictionary Essentials

**Definition**: A dictionary stores key–value pairs. Keys are unique and hashable; values can be any type.

### 🔹 Create
```python
d = {"id": 1, "name": "A"}
e = dict(code=101, dept="IT")
```

### 🔹 Access / Update
```python
d["name"]           # KeyError if missing
d.get("name", "NA") # Safe access with default
d["salary"] = 50000  # Add or update
```

### 🔹 Remove
```python
del d["id"]         # Delete key
d.pop("name", None)  # Remove with default
d.clear()            # Remove all
```

### 🔹 Merge Dictionaries
```python
a = {"x": 1}
b = {"y": 2, "x": 9}
a | b            # {'x': 9, 'y': 2}  (Py 3.9+)
a.update(b)      # In-place merge; returns None
```

### 🔍 Sort Dictionary (view as list)
```python
d = {"c": 3, "a": 1, "b": 2}
sorted(d.items())                       # By key
sorted(d.items(), key=lambda kv: kv[1]) # By value
```

### 🔍 Check Existence / Iterate
```python
"name" in d        # True if key exists
for k, v in d.items():
    pass
```

### 🚀 Advanced Dictionary Patterns

#### 🧩 Nested Dictionaries (create/access/update/delete)
```python
people = {
    1: {"name": "krutarth", "roll": 21},
    2: {"name": "het", "roll": 63},
}
# Access
people[1]["name"]           # "krutarth"
# Create / update nested
people[3] = {}
people[3]["name"] = "superman"
people[3]["roll"] = 7
# Delete nested key / whole entry
del people[3]["roll"]
del people[2]
```

#### 🔁 Nested Iteration over dict of dicts
```python
for pid, info in people.items():
    print("key:", pid)
    for k in info:
        print(k, ":", info[k])
```

#### ➕➗ Sum and Product of numeric keys/values
```python
d = {1: 2, 2: 90, 3: 50}
sum(d.values())   # 142
sum(d.keys())     # 6
prod = 1
for v in d.values():
    prod *= v       # 9000
```

#### 📊 Frequency count of values
```python
d = {1: 20, 2: 30, 3: 40, 4: 20}
freq = {}
for v in d.values():
    freq[v] = freq.get(v, 0) + 1
# freq -> {20: 2, 30: 1, 40: 1}
```

#### 🧹 Remove duplicate values (keep first occurrence)
```python
d = {1: "het", 2: "krutarth", 3: "superman", 4: "het"}
unique = {}
seen = set()
for k, v in d.items():
    if v not in seen:
        unique[k] = v
        seen.add(v)
# unique -> {1: 'het', 2: 'krutarth', 3: 'superman'}
```

#### 🔢 Sorting only the values
```python
od = {1: 25, 2: 23, 3: 21}
sorted_vals = sorted(od.values())  # [21, 23, 25]
```

#### ✏️ Modify value by key (from user input)
```python
d = {1: 20, 2: 30}
key = int(input("Enter key: "))
val = int(input("Enter value: "))
d[key] = val
```
---

## 📋 List Quick Patterns

**Definition**: Frequent list tasks that appear in exams, kept short and simple.

### 🔹 Remove Duplicates
```python
lst = [1, 2, 2, 3]
list(dict.fromkeys(lst))  # Preserves order: [1, 2, 3]
list(set(lst))            # Unordered unique
```

### 🔹 Count Elements
```python
lst.count(2)              # Count a single value
from collections import Counter
Counter(lst)              # {1:1, 2:2, 3:1}
```

### 🔹 Multiply All Elements
```python
import math
math.prod([1, 2, 3, 4])   # 24  (Py 3.8+)

prod = 1
for n in [1, 2, 3, 4]:
    prod *= n             # 24
```

### 🔹 First N Terms (simple loops)
```python
n = 5
[i for i in range(1, n+1)]  # 1..n
```

---

## 💾 File Handling

**Definition**: Python provides built-in functions to read from and write to files using `open()`.

### 📂 Opening a File
```python
# Open a file in read mode
nf = open("emp.txt", "r")
```
Mode | Description
---- | -----------
`"r"` | Read (default)
`"w"` | Write (truncate if exists / create new)
`"a"` | Append (create if not exists)
`"x"` | Create and fail if file exists
`"b"` | Binary mode (e.g., "rb")

### 📖 Reading a File (from `067_File_Open.py`)
```python
f = open("emp.txt", "r")
for line in f:
    empno, name, salary = line.split(",")
    print(empno, name, salary)
f.close()
```

### ✍️ Writing to a File
```python
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
```
Using `with` automatically closes the file when the block ends.

---

## ⚠️ Exception Handling

**Definition**: Handle runtime errors gracefully using `try`/`except` (and optional `else`/`finally`).

**Syntax**:
```python
try:
    # risky code
except ExceptionType as e:
    # handle error
else:
    # runs if no exception
finally:
    # always runs
```

**Example**:
```python
try:
    x = int("12a")
except ValueError as e:
    print("Invalid number:", e)
```

---

## 🧭 Assertions

**Definition**: `assert` checks a condition during development; raises `AssertionError` if false.

**Syntax**:
```python
assert condition, "optional message"
```

**Example**:
```python
age = 20
assert age >= 0, "age must be non-negative"
```

---

## 🔧 Functions

**Definition**: Reusable blocks of code defined with `def`, optionally returning values.

**Syntax**:
```python
def name(params):
    """docstring"""
    # body
    return value
```

**Example**:
```python
def add(a, b):
    return a + b
print(add(2, 3))  # 5
```

---

## 🧾 Docstrings

**Definition**: String literals under a definition used to document modules, classes, and functions.

**Syntax**:
```python
def func():
    """Short description.

    Optional details.
    """
    pass
```

**Example**:
```python
def greet(name):
    """Return greeting for a name."""
    return f"Hello, {name}!"
```

---

## ⭐ Arbitrary Positional Arguments

**Definition**: Use `*args` to accept variable number of positional arguments.

**Syntax**:
```python
def func(*args):
    # args is a tuple
    pass
```

**Example**:
```python
def total(*nums):
    return sum(nums)
print(total(1, 2, 3))  # 6
```

---

## 🔁 Recursion
**Definition**: A function calling itself to solve a problem by reducing it to smaller subproblems. Requires a base case to stop.

**Syntax (pattern)**:
```python
def rec(params):
    if base_condition:
        return base_value
    # work + recursive call
    return combine(rec(smaller_params))
```

**Examples**:
```python
# Fibonacci
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Factorial
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)
```

---

## 🔄 Call by Value vs Reference (Python)

**Definition**: Python uses call-by-object-reference. Mutating mutable args affects caller; rebinding names does not.

**Syntax**:
```python
def modify(seq, x):
    seq.append(x)   # mutates (visible outside)
    x = 99          # rebinds local only
```

**Example**:
```python
lst, n = [1, 2], 5
modify(lst, n)
print(lst, n)  # [1, 2, 5]  5
```

---

## 🎯 Advanced Function Concepts

### 🔧 Function Facts
**Definition**: Functions in Python are first-class objects that can be stored in variables, passed as arguments, and manipulated like any other object.

```python
def greet():
    return "Hello"

# Function as variable
func_var = greet
print(func_var())  # Outputs: Hello

# Function in list
func_list = [greet, 1, 2]

# Function in dictionary
func_dict = {greet: "greeting", "key": "value"}

# Function as argument
def call_func(func):
    return func()

print(call_func(greet))  # Outputs: Hello
```

### 🏗️ Nested Functions
**Definition**: Functions defined inside other functions. Inner functions have access to variables in the outer function's scope.

```python
def outer_func(text):
    def inner_func():
        return text.upper()
    return inner_func()

print(outer_func("hello"))  # Outputs: HELLO
```

### 🔍 Magic Methods
**Definition**: Special methods that provide information about function objects.

```python
def my_func():
    pass

print(my_func.__name__)  # Outputs: my_func
print(id(my_func))       # Outputs: memory address
```

---

## 🎨 Decorators

### 🎭 Basic Decorator
**Definition**: A decorator is a function that takes another function and extends its behavior without explicitly modifying it.

**Syntax**:
```python
@decorator_name
def function_name():
    pass
```

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        result = func()
        print("After function call")
        return result
    return wrapper

@my_decorator
def greet():
    return "Hello World!"

greet()  # Outputs: Before function call, Hello World!, After function call
```

### 🔄 Null Decorator
**Definition**: A decorator that returns the function unchanged, useful for conditional decoration.

```python
def null_decorator(func):
    return func

@null_decorator
def greet():
    return "Hello"

print(greet())  # Outputs: Hello
```

---

## 🔄 Generators

### ⚡ Generator Functions
**Definition**: Functions that use `yield` instead of `return` to produce a sequence of values lazily (one at a time).

**Syntax**:
```python
def generator_function():
    yield value1
    yield value2
    yield value3
```

```python
def number_generator():
    yield 1
    yield 2
    yield 3

# Using generator
for num in number_generator():
    print(num)  # Outputs: 1, 2, 3

# Generator object
gen = number_generator()
print(next(gen))  # Outputs: 1
print(next(gen))  # Outputs: 2
```

### 💡 Generator Benefits
- **Memory Efficient**: Values are generated on-demand
- **Lazy Evaluation**: Only computes values when needed
- **Infinite Sequences**: Can represent infinite data streams

---

## 📦 Modules and Imports

### 📚 Module Basics
**Definition**: A module is a file containing Python code that can be imported and used in other programs.

### 🔄 Import Methods

#### 1. Basic Import
```python
import module_name
module_name.function_name()
```

#### 2. Import with Alias
```python
import module_name as alias
alias.function_name()
```

#### 3. Import Specific Functions
```python
from module_name import function_name
function_name()
```

#### 4. Import All Functions
```python
from module_name import *
function_name()
```

### 📝 Example Usage
```python
# Using Circle module
import Circle
print(Circle.area(5))           # Using module.function

import Circle as C
print(C.circumference(5))       # Using alias

from Circle import area
print(area(5))                  # Direct function call

from Circle import *
print(volume(5))                # All functions available
```

---

## 🧮 Built-in Math Functions

### 📊 Math Module
**Definition**: The `math` module provides mathematical functions and constants.

```python
import math

# Ceiling and Floor
math.ceil(2.1)    # Outputs: 3 (round up)
math.floor(2.9)   # Outputs: 2 (round down)

# Absolute value
math.fabs(-5.5)   # Outputs: 5.5

# Mathematical operations
math.factorial(5) # Outputs: 120
math.sqrt(16)     # Outputs: 4.0
math.pow(2, 3)    # Outputs: 8.0
math.log(10)      # Natural logarithm

# Greatest Common Divisor
math.gcd(15, 25)  # Outputs: 5
```

### 🔢 Common Math Functions
| Function | Description | Example |
|----------|-------------|---------|
| `ceil(x)` | Round up to nearest integer | `ceil(2.1)` → `3` |
| `floor(x)` | Round down to nearest integer | `floor(2.9)` → `2` |
| `fabs(x)` | Absolute value | `fabs(-5)` → `5.0` |
| `sqrt(x)` | Square root | `sqrt(16)` → `4.0` |
| `pow(x, y)` | x raised to power y | `pow(2, 3)` → `8.0` |
| `factorial(x)` | Factorial of x | `factorial(5)` → `120` |

---

## 🔤 String Module

### 📝 String Constants
**Definition**: The `string` module provides useful constants for string operations.

```python
import string

# Available constants
print(string.ascii_letters)    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)           # 0123456789
print(string.punctuation)      # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### 🎯 Common Use Cases
- Password generation
- Input validation
- Character classification
- Text processing

---

## 🎲 Random Module

### 🎯 Random Number Generation
**Definition**: The `random` module provides functions for generating random numbers and making random choices.

```python
import random

# Random float between 0 and 1
random.random()

# Random integer in range
random.randint(1, 10)     # Random int between 1 and 10 (inclusive)

# Random choice from sequence
random.choice([1, 2, 3, 4, 5])

# Random sample
random.sample([1, 2, 3, 4, 5], 3)  # 3 random elements

# Shuffle list in place
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
```

---

## 🔐 Password Generation

### 🔑 Random Password Algorithm
**Definition**: Combining `random` and `string` modules to generate secure passwords.

```python
import random
import string

def generate_password(length):
    # Character pool
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Usage
password = generate_password(12)
print(password)  # Example: aB3$xY9@mN2!
```

### 🛡️ Password Components
- **Letters**: `string.ascii_letters` (a-z, A-Z)
- **Digits**: `string.digits` (0-9)
- **Symbols**: `string.punctuation` (special characters)

---

## 📐 Pascal's Triangle

### 🔺 Pascal's Triangle Algorithm
**Definition**: A triangular array where each number is the sum of the two numbers above it, calculated using combinations (nCr).

**Formula**: `nCr = n! / (r! * (n-r)!)`

```python
from math import factorial

def pascal_triangle(n):
    for i in range(n):
        # Left padding
        for j in range(n - i + 1):
            print(end=" ")
        
        # Print values
        for j in range(i + 1):
            value = factorial(i) // (factorial(j) * factorial(i - j))
            print(value, end=" ")
        
        print()  # New line

pascal_triangle(5)
```

### 📋 Algorithm Steps
1. Take number of rows (n)
2. For each row i from 0 to n:
   - Add left spacing
   - Calculate nCr for each position j
   - Print the value
   - Move to next line

---

## 🔤 Pangram Algorithm

### 🔍 Pangram Detection
**Definition**: A pangram is a sentence containing every letter of the alphabet at least once.

```python
import string

def is_pangram(sentence):
    # Convert to lowercase
    sentence = sentence.lower()
    
    # Get unique alphabetic characters
    letters = set(filter(str.isalpha, sentence))
    
    # Check if all 26 letters are present
    return len(letters) == 26

# Test
text = "The quick brown fox jumps over the lazy dog"
print(is_pangram(text))  # Outputs: True
```

### 📋 Algorithm Steps
1. Convert sentence to lowercase
2. Filter only alphabetic characters
3. Create set of unique letters
4. Check if set contains all 26 alphabet letters

---

## 🧠 Common Algorithms

### 🔢 Maximum of Three Numbers
```python
def max_of_three(a, b, c):
    return max(a, b, c)
```

### ➕ Sum of List Elements
```python
def sum_list(nums):
    return sum(nums)
```

### ✖️ Product of List Elements
```python
def multiply_list(nums):
    result = 1
    for num in nums:
        result *= num
    return result
```

### 🔄 String Reversal
```python
def reverse_string(s):
    return s[::-1]
```

### 📊 Range Check
```python
def in_range(num, start, end):
    return start <= num <= end
```

### 🎯 Remove Duplicates
```python
def remove_duplicates(nums):
    return list(set(nums))
```

### 🔢 Even Numbers Filter
```python
def get_even_numbers(nums):
    return [num for num in nums if num % 2 == 0]
```

### 🔤 Sort Hyphen-Separated Words
```python
def sort_hyphenated(text):
    words = text.split("-")
    words.sort()
    return "-".join(words)
```

### 2️⃣ Prime Number Check
```python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```

### 🔄 Palindrome Check
```python
def is_palindrome(s):
    return s == s[::-1]
```

---

## 📁 Advanced File Handling

### 📂 File Object Properties
**Definition**: File objects have built-in attributes that provide information about the file's state and properties.

```python
f = open("data.txt", "r")

# File properties
print(f.name)     # Outputs: data.txt (filename)
print(f.mode)     # Outputs: r (file mode)
print(f.closed)   # Outputs: False (file status)
print(f.errors)   # Error handling method

f.close()
print(f.closed)   # Outputs: True (after closing)
```

### 📖 File Reading Methods

#### 1. `read()` Method
**Definition**: Reads specified number of characters from file, or entire file if no parameter given.

```python
f = open("data.txt", "r")
content = f.read(20)    # Read first 20 characters
all_content = f.read()  # Read entire file
f.close()
```

#### 2. `readline()` Method
**Definition**: Reads one line at a time from the file and returns it as a string.

```python
f = open("data.txt", "r")
first_line = f.readline()  # Returns first line as string
print(type(first_line))    # <class 'str'>
f.close()
```

#### 3. `readlines()` Method
**Definition**: Reads all lines from file and returns them as a list of strings.

```python
f = open("data.txt", "r")
all_lines = f.readlines()  # Returns list of all lines
print(type(all_lines))     # <class 'list'>
print(len(all_lines))      # Number of lines
f.close()
```

### 🎯 File Pointer Methods

#### `tell()` Method
**Definition**: Returns current position of file pointer (cursor) in the file.

```python
f = open("data.txt", "r")
position = f.tell()  # Returns current position (integer)
print(position)      # Outputs: 0 (at beginning)
f.close()
```

#### `seek()` Method
**Definition**: Moves file pointer to specified position in the file.

```python
f = open("data.txt", "r")
f.seek(10)          # Move pointer to position 10
content = f.read()  # Read from position 10 onwards
f.close()
```

### ✍️ File Writing Methods

#### Write Mode (`"w"`)
**Definition**: Opens file for writing, overwrites existing content.

```python
f = open("data.txt", "w")
f.write("Hello World\n")
f.write("Python Programming")
f.close()
```

#### Append Mode (`"a"`)
**Definition**: Opens file for writing, adds content to the end without overwriting.

```python
f = open("data.txt", "a")
f.write("New line\n")
f.write("Another line")
f.close()
```

### 🔢 Binary Mode
**Definition**: Opens file in binary mode for reading/writing binary data.

```python
# Binary read
f = open("data.txt", "rb")
binary_data = f.read()
print(type(binary_data))  # <class 'bytes'>
f.close()

# Binary write
f = open("data.txt", "wb")
f.write(b"Binary content")
f.close()
```

### 📊 CSV File Handling
**Definition**: Working with comma-separated values for structured data storage.

```python
# Writing CSV data
f = open("employees.csv", "w")
f.write("Name,Salary,Department\n")
f.write("John,50000,IT\n")
f.write("Alice,60000,HR\n")
f.close()

# Reading CSV data
f = open("employees.csv", "r")
for line in f:
    name, salary, dept = line.strip().split(",")
    print(f"Name: {name}, Salary: {salary}")
f.close()
```

---

## 📋 File CRUD Operations

### 🏗️ CRUD Overview
**Definition**: CRUD stands for Create, Read, Update, Delete - the four basic operations for data management.

### 1. 📝 Create Operation
**Definition**: Adding new records to a file.

```python
def create_record():
    f = open("data.txt", "a")
    name = input("Enter name: ")
    age = input("Enter age: ")
    f.write(f"{name},{age}\n")
    f.close()
    print("Record created successfully!")
```

### 2. 📖 Read Operation
**Definition**: Displaying all records from a file.

```python
def read_records():
    try:
        f = open("data.txt", "r")
        print("All Records:")
        for line in f:
            print(line.strip())
        f.close()
    except FileNotFoundError:
        print("File not found!")
```

### 3. ✏️ Update Operation
**Definition**: Modifying existing records in a file by creating a temporary file.

```python
def update_record():
    search_id = input("Enter ID to update: ")
    new_value = input("Enter new value: ")
    
    f = open("data.txt", "r")
    temp_f = open("temp.txt", "w")
    
    for line in f:
        record_id, data = line.strip().split(",", 1)
        if record_id == search_id:
            temp_f.write(f"{record_id},{new_value}\n")
            print("Record updated!")
        else:
            temp_f.write(line)
    
    f.close()
    temp_f.close()
```

### 4. 🗑️ Delete Operation
**Definition**: Removing specific records from a file.

```python
def delete_record():
    search_id = input("Enter ID to delete: ")
    
    f = open("data.txt", "r")
    temp_f = open("temp.txt", "w")
    found = False
    
    for line in f:
        record_id, data = line.strip().split(",", 1)
        if record_id == search_id:
            print(f"Record {record_id} deleted!")
            found = True
        else:
            temp_f.write(line)
    
    f.close()
    temp_f.close()
    
    if not found:
        print("Record not found!")
```

### 🔄 Menu-Driven CRUD System
**Definition**: A complete system combining all CRUD operations with user menu.

```python
def file_crud_menu():
    while True:
        print("\n=== File CRUD Menu ===")
        print("1. Create Record")
        print("2. Read Records") 
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            create_record()
        elif choice == 2:
            read_records()
        elif choice == 3:
            update_record()
        elif choice == 4:
            delete_record()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
```

### 💡 CRUD Best Practices
- **Always close files** after operations
- **Use try-except** for error handling
- **Create temporary files** for update/delete operations
- **Validate user input** before processing
- **Provide user feedback** for all operations

### 🔧 File Operation Modes Summary
| Mode | Description | Use Case |
|------|-------------|----------|
| `"r"` | Read only | Reading existing files |
| `"w"` | Write (overwrite) | Creating new files |
| `"a"` | Append | Adding to existing files |
| `"rb"` | Binary read | Reading binary files |
| `"wb"` | Binary write | Writing binary files |

---

## 🔢 Binary File Operations

### 🔐 Binary Mode CRUD
**Definition**: File operations using binary mode for handling data as bytes instead of text strings.

### 📝 Binary Write Operations
**Definition**: Writing data to files in binary format using encode/decode methods.

```python
# Binary append mode
f = open("data.txt", "ab")
text = "Hello World\n"
f.write(text.encode('utf-8'))  # Convert string to bytes
f.close()

# Binary write mode
f = open("data.txt", "wb")
data = "New content"
f.write(data.encode('utf-8'))
f.close()
```

### 📖 Binary Read Operations
**Definition**: Reading binary data and converting it back to readable text format.

```python
# Binary read mode
f = open("data.txt", "rb")
for line in f:
    text = line.decode('utf-8').strip()  # Convert bytes to string
    print(text)
f.close()

# Read all binary data
f = open("data.txt", "rb")
binary_data = f.read()
text_data = binary_data.decode('utf-8')
f.close()
```

### 🔄 Binary CRUD Operations
**Definition**: Complete Create, Read, Update, Delete operations using binary file modes.

```python
# Create (Binary)
def create_binary_record():
    f = open("records.txt", "ab")
    data = "ID,Name,Value\n"
    f.write(data.encode('utf-8'))
    f.close()

# Read (Binary)
def read_binary_records():
    f = open("records.txt", "rb")
    for line in f:
        print(line.decode('utf-8').strip())
    f.close()

# Update (Binary)
def update_binary_record():
    f = open("records.txt", "rb")
    temp_f = open("temp.txt", "wb")
    for line in f:
        decoded_line = line.decode('utf-8')
        # Process and write back
        temp_f.write(decoded_line.encode('utf-8'))
    f.close()
    temp_f.close()
```

### 💡 Binary Mode Benefits
- **Encoding Control**: Handle different character encodings
- **Data Integrity**: Preserve exact byte sequences
- **Performance**: Faster for large files
- **Compatibility**: Work with non-text files

---

## 🎯 Variable Scoping

### 🏠 Local Scope
**Definition**: Variables defined inside a function that are only accessible within that function.

```python
def my_function():
    x = 10  # Local variable
    print(x)  # Outputs: 10

x = 5  # Global variable
my_function()
print(x)  # Outputs: 5 (global x unchanged)
```

### 🌍 Global Scope
**Definition**: Variables defined outside functions that are accessible throughout the program.

```python
x = 10  # Global variable

def my_function():
    print(x)  # Accesses global x
    
my_function()  # Outputs: 10
```

### 🔧 Global Keyword
**Definition**: The `global` keyword allows modification of global variables inside functions.

**Syntax**:
```python
global variable_name
```

```python
x = 10  # Global variable

def modify_global():
    global x
    x = 20  # Modifies global x
    print("Inside function:", x)

modify_global()  # Outputs: Inside function: 20
print("Outside function:", x)  # Outputs: Outside function: 20
```

### 🔄 Scope Resolution
**Definition**: Python follows LEGB rule - Local, Enclosing, Global, Built-in scope resolution.

```python
def outer_function():
    x = 20  # Enclosing scope
    
    def inner_function():
        x = 30  # Local scope
        print("Inner x:", x)  # Outputs: 30
    
    inner_function()
    print("Outer x:", x)  # Outputs: 20

x = 10  # Global scope
outer_function()
print("Global x:", x)  # Outputs: 10
```

### ⚠️ Scope Best Practices
- **Minimize global variables** for better code organization
- **Use function parameters** instead of global variables when possible
- **Be explicit** with `global` keyword when modifying global variables
- **Avoid variable name conflicts** between different scopes

---

## 📝 Advanced File Methods

### 📋 writelines() Method
**Definition**: Writes a list of strings to a file without adding newline characters automatically.

```python
# Writing multiple lines
lines = ['First line\n', 'Second line\n', 'Third line\n']
f = open("output.txt", "w")
f.writelines(lines)
f.close()

# Without newlines (manual addition needed)
data = ['Hello', 'World', 'Python']
f = open("output.txt", "w")
f.writelines([line + '\n' for line in data])
f.close()
```

### 🔒 Context Manager (with statement)
**Definition**: Automatic file handling that ensures files are properly closed even if errors occur.

**Syntax**:
```python
with open(filename, mode) as file_object:
    # File operations
```

```python
# Automatic file closing
with open("data.txt", "w") as f:
    f.write("Hello World")
# File automatically closed here

# Multiple files
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    data = infile.read()
    outfile.write(data.upper())
```

### ⚠️ File Exception Handling
**Definition**: Proper error handling for file operations using try-except blocks.

```python
try:
    f = open("nonexistent.txt", "r")
    content = f.read()
    f.close()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File operation completed")
```

### 🔄 Complete Exception Handling Pattern
```python
def safe_file_operation(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except PermissionError:
        print(f"No permission to read {filename}")
        return None
    finally:
        print("File operation attempt completed")
```

---

## 📊 File Analysis Operations

### 📏 Line Counting
**Definition**: Counting total number of lines in a file for analysis.

```python
# Count total lines
f = open("data.txt", "r")
lines = f.readlines()
total_lines = len(lines)
print(f"Total lines: {total_lines}")
f.close()

# Get specific line ranges
n = 3
first_n_lines = lines[:n]  # First 3 lines
last_n_lines = lines[-n:]  # Last 3 lines
```

### 🔤 Character Counting
**Definition**: Analyzing character count and content in files.

```python
# Count characters
f = open("data.txt", "r")
content = f.read()
char_count = len(content)
print(f"Total characters: {char_count}")
f.close()

# Count specific characters
letter_count = sum(1 for char in content if char.isalpha())
digit_count = sum(1 for char in content if char.isdigit())
```

### 📋 Line Range Operations
**Definition**: Extracting specific ranges of lines from files.

```python
def get_line_range(filename, start, end):
    with open(filename, "r") as f:
        lines = f.readlines()
        return lines[start:end]

# Get lines 5-10
selected_lines = get_line_range("data.txt", 4, 10)

# Get first n lines
def get_first_lines(filename, n):
    with open(filename, "r") as f:
        return [f.readline() for _ in range(n)]
```

### 📈 File Statistics
**Definition**: Comprehensive analysis of file content and structure.

```python
def analyze_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        content = ''.join(lines)
    
    stats = {
        'total_lines': len(lines),
        'total_chars': len(content),
        'total_words': len(content.split()),
        'empty_lines': sum(1 for line in lines if line.strip() == ''),
        'avg_line_length': sum(len(line) for line in lines) / len(lines)
    }
    return stats
```

---

## 🔧 File Utility Functions

### 📄 File Copying
**Definition**: Copying content from one file to another file.

```python
def copy_file(source, destination):
    with open(source, "r") as src, open(destination, "w") as dest:
        for line in src:
            dest.write(line)
    print("File copied successfully")

# Usage
copy_file("source.txt", "backup.txt")
```

### 📋 File to List Conversion
**Definition**: Reading file content and storing each line as a list element.

```python
def file_to_list(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f]

# Usage
lines_list = file_to_list("data.txt")
print(lines_list)
```

### 🔍 Find Longest Word
**Definition**: Analyzing file content to find the longest word.

```python
def find_longest_word(filename):
    longest = ""
    with open(filename, "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                if len(word) > len(longest):
                    longest = word
    return longest

# Usage
longest_word = find_longest_word("text.txt")
print(f"Longest word: {longest_word}")
```

### 📏 File Size Operations
**Definition**: Getting file size information using the os module.

```python
import os

def get_file_size(filename):
    try:
        size = os.path.getsize(filename)
        return size
    except FileNotFoundError:
        return None

# Usage
size = get_file_size("data.txt")
print(f"File size: {size} bytes")
```

### 🔗 Line Combination
**Definition**: Reading and combining specific lines from files.

```python
def combine_lines(filename, line1_num, line2_num):
    with open(filename, "r") as f:
        lines = f.readlines()
        if len(lines) >= max(line1_num, line2_num):
            line1 = lines[line1_num - 1].strip()
            line2 = lines[line2_num - 1].strip()
            return line1 + " " + line2
    return None

# Combine first two lines
def combine_first_two_lines(filename):
    with open(filename, "r") as f:
        line1 = f.readline().strip()
        line2 = f.readline().strip()
        return line1 + " " + line2
```

### 📊 Dictionary File Operations
**Definition**: Working with structured data using dictionaries and files.

```python
# Employee data processing
def process_employee_data():
    employees = {
        0: [1, "Alice", 5000],
        1: [2, "Bob", 6000], 
        2: [3, "Charlie", 7000]
    }
    
    total_salary = 0
    for key, value in employees.items():
        emp_id, name, salary = value
        total_salary += salary
        print(f"Employee: {name}, Salary: {salary}")
    
    print(f"Total Salary: {total_salary}")
    return total_salary
```

---

## 🏛️ Object-Oriented Programming (OOP)

### 📋 OOP Core Concepts
**Definition**: Object-Oriented Programming is a programming paradigm based on objects that contain data and code.

### 🔑 Key OOP Terms
| Term | Definition |
|------|------------|
| **Class** | Blueprint or template for creating objects |
| **Object** | Instance of a class (real-world entity) |
| **Attributes** | Properties or data stored in an object |
| **Methods** | Functions defined inside a class |
| **self** | Reference to the current instance of the class |
| **Constructor** | Special method `__init__()` to initialize objects |

---

## 🎓 Classes and Objects

### 📘 Class Definition
**Definition**: A class is a user-defined blueprint for creating objects with shared attributes and methods.

**Syntax**:
```python
class ClassName:
    # class body
    pass
```

```python
# Define a class
class Student:
    name = "Default"  # Class attribute
    
    def display(self):
        print(f"Student: {self.name}")

# Create objects
student1 = Student()
student2 = Student()

print(type(student1))  # <class '__main__.Student'>
```

### 🎯 Creating Objects
**Definition**: Objects are instances of a class created using the class name followed by parentheses.

```python
class Car:
    color = "Red"

# Creating objects
car1 = Car()
car2 = Car()

print(car1.color)  # Red
print(car2.color)  # Red
```

---

## 🔧 Class Methods and Attributes

### 📦 Class Attributes
**Definition**: Variables shared by all instances of a class, defined directly in the class.

```python
class Student:
    school = "ABC School"  # Class attribute (shared)
    
    def __init__(self, name):
        self.name = name  # Instance attribute (unique)

s1 = Student("Alice")
s2 = Student("Bob")

print(s1.school)  # ABC School (shared)
print(s2.school)  # ABC School (shared)
print(s1.name)    # Alice (unique)
print(s2.name)    # Bob (unique)
```

### 🎯 Instance Attributes
**Definition**: Variables unique to each object instance, typically defined in `__init__`.

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

p1 = Person("John", 25)
p2 = Person("Jane", 30)
```

### 📊 Class Variable Counter
**Definition**: Using class variables to track the number of instances created.

```python
class Student:
    count = 0  # Class variable
    
    def __init__(self, name):
        self.name = name
        Student.count += 1

s1 = Student("Alice")
s2 = Student("Bob")
print(Student.count)  # 2
```

### 📝 Instance Methods
**Definition**: Functions defined inside a class that operate on instance data.

```python
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

calc = Calculator()
print(calc.add(5, 3))       # 8
print(calc.subtract(10, 4))  # 6
```

---

## 🏗️ Constructors and self

### 🔨 Constructor (`__init__`)
**Definition**: Special method automatically called when an object is created to initialize attributes.

**Syntax**:
```python
def __init__(self, parameters):
    # initialization code
```

```python
class Account:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

acc = Account("John", 1000)
print(acc.holder)   # John
print(acc.balance)  # 1000
```

### 🔍 The `self` Parameter
**Definition**: Reference to the current instance of the class, used to access instance attributes and methods.

```python
class Person:
    def __init__(self, name):
        self.name = name  # self refers to the object
    
    def greet(self):
        print(f"Hello, I am {self.name}")

p = Person("Alice")
p.greet()  # Hello, I am Alice
```

### 💰 Account Class Example
**Definition**: Real-world banking account with deposit, withdraw, and transfer operations.

```python
class Account:
    def __init__(self, holder, number, balance, credit_line=1500):
        self.holder = holder
        self.number = number
        self.balance = balance
        self.credit_line = credit_line
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance - amount < -self.credit_line:
            return False
        self.balance -= amount
        return True
    
    def transfer(self, target, amount):
        if self.withdraw(amount):
            target.deposit(amount)
            return True
        return False

# Usage
acc1 = Account("Alice", "123", 1000)
acc2 = Account("Bob", "456", 500)
acc1.transfer(acc2, 200)
```

### 📚 Docstrings
**Definition**: Documentation strings for classes and methods accessed via `__doc__`.

```python
class Person:
    """This class represents a person with name and age"""
    def __init__(self, name):
        self.name = name

print(Person.__doc__)  # This class represents a person...
```

---

## 🧬 Inheritance

### 👨‍👩‍👦 Inheritance Basics
**Definition**: Mechanism where a new class (child) derives properties and methods from an existing class (parent).

**Syntax**:
```python
class ParentClass:
    pass

class ChildClass(ParentClass):
    pass
```

### 🔗 Single Inheritance
**Definition**: A child class inherits from a single parent class.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age)  # Call parent constructor
        self.roll_no = roll_no
        self.marks = marks
    
    def show_details(self):
        print(f"Roll No: {self.roll_no}, Marks: {self.marks}")

# Usage
s = Student("Alice", 20, 101, 95)
s.display()       # Inherited method
s.show_details()  # Child class method
```

### 🔝 super() Function
**Definition**: Built-in function to call methods from the parent class.

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call parent's __init__
        self.age = age
```

### 💡 Inheritance Benefits
- **Code Reusability**: Reuse parent class code
- **Extensibility**: Add new features to existing classes
- **Organization**: Logical hierarchy of classes
- **Maintenance**: Changes in parent reflect in children

---

## 🔀 Polymorphism

### 🎭 Polymorphism Concept
**Definition**: Ability to use a common interface for different data types or objects.

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Bird:
    def speak(self):
        return "Chirp!"

# Polymorphic function
def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
bird = Bird()

animal_sound(dog)   # Woof!
animal_sound(cat)   # Meow!
animal_sound(bird)  # Chirp!
```

### 🔄 Method Resolution
**Definition**: Python uses Method Resolution Order (MRO) to determine which method to call.

```python
class Person:
    def show(self):
        print("I am a Person")

class Teacher(Person):
    def show(self):
        print("I am a Teacher")

p = Person()
t = Teacher()
p.show()  # I am a Person
t.show()  # I am a Teacher
```

---

## 🔒 Encapsulation

### 🛡️ Data Hiding
**Definition**: Restricting access to certain attributes and methods by making them private.

**Syntax**:
```python
self.__attribute  # Private attribute (name mangling)
self._attribute   # Protected attribute (convention)
```

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

acc = Account(1000)
acc.deposit(500)
print(acc.get_balance())  # 1500
# print(acc.__balance)    # AttributeError
```

### 🔐 Access Modifiers
| Type | Syntax | Access Level |
|------|--------|--------------|
| Public | `self.attribute` | Accessible everywhere |
| Protected | `self._attribute` | Convention (still accessible) |
| Private | `self.__attribute` | Name mangling (harder to access) |

```python
class MyClass:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"

obj = MyClass()
print(obj.public)     # ✅ Works
print(obj._protected) # ✅ Works (convention only)
# print(obj.__private) # ❌ AttributeError
```

---

## 🎭 Abstraction

### 🎨 Abstract Classes
**Definition**: Classes that cannot be instantiated and serve as blueprints for other classes.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(5, 3)
print(rect.area())       # 15
print(rect.perimeter())  # 16
```

### 📋 Abstract Methods
**Definition**: Methods declared in abstract class but implemented in child classes.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

dog = Dog()
print(dog.make_sound())  # Bark
```

---

## ⚙️ Operator Overloading

### ➕ Overloading Operators
**Definition**: Defining custom behavior for operators (+, -, *, etc.) in user-defined classes.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2  # Calls __add__
print(p3)  # Point(6, 8)
```

### 🔢 Common Magic Methods
| Operator | Method | Example |
|----------|--------|---------|
| `+` | `__add__` | `obj1 + obj2` |
| `-` | `__sub__` | `obj1 - obj2` |
| `*` | `__mul__` | `obj1 * obj2` |
| `/` | `__truediv__` | `obj1 / obj2` |
| `==` | `__eq__` | `obj1 == obj2` |
| `<` | `__lt__` | `obj1 < obj2` |
| `str()` | `__str__` | `str(obj)` |
| `repr()` | `__repr__` | `repr(obj)` |

---

## 🔄 Method Overloading and Overriding

### 🔁 Method Overriding
**Definition**: Redefining a parent class method in the child class with the same name.

```python
class Parent:
    def show(self):
        print("Parent class method")

class Child(Parent):
    def show(self):
        print("Child class method (Overridden)")

c = Child()
c.show()  # Child class method (Overridden)
```

### 🔄 Method Overloading (Simulated)
**Definition**: Python doesn't support traditional method overloading, but it can be simulated using default arguments.

```python
class Calculator:
    def add(self, a=None, b=None, c=None):
        if a and b and c:
            return a + b + c
        elif a and b:
            return a + b
        else:
            return a

calc = Calculator()
print(calc.add(2, 3))      # 5
print(calc.add(2, 3, 4))   # 9
```

### 📚 List-based Class with CRUD
**Definition**: Creating a class to manage a set of integers with insert, member, remove operations.

```python
class IntSet:
    def __init__(self):
        self.vals = []
    
    def insert(self, e):
        if e not in self.vals:
            self.vals.append(e)
    
    def member(self, e):
        return e in self.vals
    
    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(f"{e} not found")
    
    def getMembers(self):
        return self.vals[:]
    
    def __str__(self):
        self.vals.sort()
        return "{" + ", ".join(str(e) for e in self.vals) + "}"

# Usage
s = IntSet()
s.insert(5)
s.insert(10)
s.insert(3)
print(s)              # {3, 5, 10}
print(s.member(5))    # True
s.remove(5)
print(s.getMembers()) # [3, 10]
```

---

<div align="center">
### 🐍 Happy Python Coding! 🐍

*"The only way to learn a programming language is by writing programs in it." - Dennis Ritchie*

</div>
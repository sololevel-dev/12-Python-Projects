#level 1 🤖
#1. Hello User
#userName=input("Enter your name: ")
#userAge=input("Enter your age: ")
#print(f"Hello {userName}! you are {userAge} years old")

#level 1 🤖
#2. Calculator
"""
Simple calculator that performs basic arithmetic operations.
Supports addition, subtraction, multiplication, and division.
Includes input validation and division by zero protection.
"""
# try:
#     firstNumber = float(input("Enter first number: "))
#     secondNumber = float(input("Enter second number: "))
#     operation = input("Enter operation (+, -, *, /): ")
    
#     if operation == "+":
#         result = firstNumber + secondNumber
#         print(f"{firstNumber} + {secondNumber} = {int(result)}")
#     elif operation == "-":
#         result = firstNumber - secondNumber
#         print(f"{firstNumber} - {secondNumber} = {int(result)}")
#     elif operation == "*":
#         result = firstNumber * secondNumber
#         print(f"{firstNumber} * {secondNumber} = {int(result)}")
#     elif operation == "/":
#         if secondNumber == 0:
#             print("Error: Division by zero is not allowed!")
#         else:
#             result = firstNumber / secondNumber
#             print(f"{firstNumber} / {secondNumber} = {int(result)}")
#     else:
#         print("Invalid operation! Please use +, -, *, or /")
# except ValueError:
#     print("Error: Please enter valid numbers!")
# except Exception as e:
#     print(f"An error occurred: {e}")

#level 1 🤖
#3. Odd or Even
# num=int(input('Enter a number: '))
# if num%2==0:
#     print('your number is Even')
# else:
#     print('your number is Odd')    


#level 2 🤖
#1. fizzBuzz
# for i in range(0,101):
#     if i%3==0 and i%5==0: #if the number is divisible by 3 and 5, print FizzBuzz
#         print('FizzBuzz')
#     elif i%3==0: #if the number is divisible by 3, print Fizz
#         print('Fizz')
#     elif i%5==0: #if the number is divisible by 5, print Buzz
#         print('Buzz')
#     else: #if the number is not divisible by 3 or 5, print the number
#         print(i)
#level 2 🤖
#2. Multiplication Table
"""
Nicely formatted multiplication table with aligned columns.
Allows user to specify the maximum number for the table.
"""
# try:
#     max_num = int(input('Enter the maximum number for multiplication table (1-20): '))
    
#     # Validate input
#     if max_num < 1 or max_num > 20:
#         print("Please enter a number between 1 and 20.")
#         max_num = 12  # Default to 12 if invalid input
    
#     # Calculate the width needed for proper alignment
#     max_product = max_num * max_num
#     width = len(str(max_product)) + 1
#     # Print header row
#     print(f"{'':<{width}}", end="")
#     for col in range(1, max_num + 1):
#         print(f"{col:>{width}}", end="")
#     print()
    
#     # Print separator line
#     print("-" * (width * (max_num + 1)))
#     # Print multiplication table
#     for row in range(1, max_num + 1):
#     #     # Print row number
#         print(f"{row:<{width}}", end="")
        
#     #     # Print products for this row
#         for col in range(1, max_num + 1):
#             product = row * col
#             print(f"{product:>{width}}", end="")
#         print()  # New line after each row

# except ValueError:
#     print("Please enter a valid number.")
# except Exception as e:
#     print(f"An error occurred: {e}")


#level 2 🤖
#3. Password Strength Checker
# import re
# def checkPasswordStrength(password):
#     if(len(password)<8):
#         return 'Weak'
#     has_letter=re.search(r'[a-zA-Z]',password) #check if password has at least on letter
#     has_digit=re.search(r'\d+',password) #check if password has at least on digit
#     has_specialEnd=re.search(r'[^a-zA-Z0-9]+$',password) #check if password has at least on special character check end of the string
#     has_special=re.search(r'[^a-zA-Z0-9]',password) #check if password has at least on special character check in the middle of the string
#     if(has_letter and has_digit and has_special):
#         return 'Strong'
#     elif(has_letter and has_digit):
#         return 'Medium'
#     else:
#         return 'Weak'

# userPassword=input('Enter your password: ')
# print(checkPasswordStrength(userPassword))

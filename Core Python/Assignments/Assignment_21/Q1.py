# 1. Develop a simple calculator program that performs basic arithmetic operations (+,
# -, *, /) on two numbers provided by the user. The program should ask the user for
# the numbers and the operator. However, the program should handle the following
# exceptions:
# a. Invalid Number: If the user enters a number that is not valid, catch the
# exception and display an error message.
# b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
# "/", catch the exception and display an error message.
# c. Division by Zero: If the user tries to divide by zero, catch the exception and
# display an error message.
# Write a program that performs the requested arithmetic operation and
# handles the exceptions as described above.


try:
    #Take numbers from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Efnter second number: "))

    #Take opearator from user
    operator = input("Enter operator (+, -, *, /): ")

    #Check operator and perform operation
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2    
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        raise ValueError("Invalid Operator")

    print("Result =", result)

# Invalid number
except ValueError as e:
    print("Error:", e)

#Division by zero
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

#Any other unexpected error
except Exception as e:
    print("Error", e)
# Simple Python Calculator

# Display a Welcome Message
print("Welcome to the Simple Python Calculator!")

# Prompt the User for Input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display Operation Options
print("Choose an operation: +, -, *, /")
operation = input("Enter your choice: ")

# Perform the Operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Undefined (division by zero is not allowed)"
else:
    result = "Invalid operation"

# Display the Result
print("The result is:", result)

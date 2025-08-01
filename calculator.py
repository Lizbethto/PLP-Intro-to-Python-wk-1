# Basic Calculator Program

# Step 1: Get user input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Step 2: Perform the operation
if operation == '+':
    result = a + b
    print(f"{a} + {a} = {result}")

elif operation == '-':
    result = a - b
    print(f"{a} - {b} = {result}")

elif operation == '*':
    result = a * b
    print(f"{a} * {b} = {result}")

elif operation == '/':
    if b != 0:
        result = a / b
        print(f"{a} / {b} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operation entered.")


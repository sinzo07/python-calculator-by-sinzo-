a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Choose operation (add/sub/mul/div): ").lower()

if operation == "add":
    print("Result is:", a + b)
elif operation == "sub":
    print("Result is:", a - b)
elif operation == "mul":
    print("Result is:", a * b)
elif operation == "div":
    if b != 0:
        print("Result is:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")
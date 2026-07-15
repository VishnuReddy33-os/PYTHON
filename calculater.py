def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("=== Python Calculator ===")
    print("Operations: +  -  *  /")
    print("Type 'exit' to quit.\n")

    while True:
        op = input("Enter operation (+, -, *, /): ")
        if op.lower() == "exit":
            print("Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.\n")
            continue

        if op == "+":
            print("Result:", add(num1, num2))
        elif op == "-":
            print("Result:", subtract(num1, num2))
        elif op == "*":
            print("Result:", multiply(num1, num2))
        elif op == "/":
            print("Result:", divide(num1, num2))
        else:
            print("Invalid operation! Try again.\n")

        print()  # blank line for readability


calculator()

import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose the operation (add, subtract, multiply, divide): ").lower()
        
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        else:
            print("Invalid operation.")
            sys.exit(1)
        
        if result is None:
            print("Cannot divide by zero.")
        else:
            print(f"The result is: {result}")
    except ValueError as e:
        print(f"Invalid input: {e}")

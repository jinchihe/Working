def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    while True:
        print("Enter two numbers and the operation to perform (add, subtract, multiply, divide) or 'exit' to quit:")
        num1 = input("First number: ")
        num2 = input("Second number: ")
        operation = input("Operation: ").lower()

        if operation == 'exit':
            break

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Invalid input: Please enter numeric values.")
            continue

        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            print("Invalid operation: Please enter a valid operation (add, subtract, multiply, divide).")
            continue

        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)

        print(f"Result: {result}")

if __name__ == "__main__":
    main()

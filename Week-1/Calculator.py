
def add(a,b):
    return a +b 

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Enter 'exit' to quit")

    while True:
        choice = input("Enter operation (+, -, *, /) 0r 'exit': ")

        if choice == 'exit':
            print("Good bye!")
            break

        if choice not in ['+', '-', '*', '/']:
            print("Invalid operation. Please try again.")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            result = add(num1, num2)

        elif choice == '-':
            result = subtract(num1, num2)

        elif choice == '*':
            result = multiply(num1, num2)
        
        elif choice == '/':
            result = divide(num1, num2)

        print("Result: ", result)

calculator()

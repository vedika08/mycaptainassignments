def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Dictionary to map operations
operations = {
    '1': (add, "+", "Add"),
    '2': (subtract, "-", "Subtract"),
    '3': (multiply, "*", "Multiply"),
    '4': (divide, "/", "Divide"),
}

def get_input():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2

# Main logic
print("Select operation:")
for key, value in operations.items():
    print(f"{key}. {value[2]}")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in operations:
        num1, num2 = get_input()
        operation_func, operator, operation_name = operations[choice]
        result = operation_func(num1, num2)
        print(f"{num1} {operator} {num2} = {result}")
        break
    else:
        print("Invalid Input, please choose a valid option.")

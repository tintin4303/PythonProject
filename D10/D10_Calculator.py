import math

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def exponent(n1, n2):
    return n1 ** n2

def divide(n1, n2):
    return n1 / n2

# def square_root(n1):
#     return math.sqrt(n1)

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    "^" : exponent,
    # "sqrt" : square_root
}
# print(operations["*"](4, 8))

while True:
    print(r"""
     _____________________
    |  _________________  |
    | |              0. | |
    | |_________________| |
    |  ___ ___ ___   ___  |
    | | 7 | 8 | 9 | | + | |
    | |___|___|___| |___| |
    | | 4 | 5 | 6 | | - | |
    | |___|___|___| |___| |
    | | 1 | 2 | 3 | | x | |
    | |___|___|___| |___| |
    | | . | 0 | = | | / | |
    | |___|___|___| |___| |
    |_____________________|
    """)
    try:
        first_num = float(input("What's the first number?: "))
    except ValueError:
        print("Invalid input! Enter a digit.")
        first_num = float(input("What's the first number?: "))
    cont = 'y'
    while cont == 'y':
        print("+\n-\n*\n/\n^")
        operation = input("Pick an operation: ")
        while operation not in operations:
            print("Choose from the provided list of operations.")
            print("+\n-\n*\n/\n^")
            operation = input("Pick an operation: ")

        next_num = float(input("What's the next number?: "))

        result = operations[operation](first_num, next_num)
        print(f"{first_num} {operation} {next_num} = {result}")
        cont = input(f"Type 'y' to continue calculating with {result}, or Type 'n' to start a new calculation: ").lower()
        while cont != 'y' and cont != 'n':
            print("Invalid input! Enter 'y' or 'n'")
            cont = input(f"Type 'y' to continue calculating with {result}, or Type 'n' to start a new calculation: ").lower()
        if cont == 'y':
            first_num = result

    end = input("Would you like to continue using the calculator?(Y/N): ").lower()
    while end != 'y' and end != 'n':
        print("Invalid input! Enter 'Y' or 'N'")
        end = input("Would you like to continue using the calculator?(Y/N): ").lower()
    if end == 'n':
        break

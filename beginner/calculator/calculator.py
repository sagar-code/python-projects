from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def mulitply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': mulitply,
    '/': divide,
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        user_call = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation "
                          f"or 'q' to quit the program:")

        if user_call == "y":
            num1 = answer
        elif user_call == 'n':
            should_continue = False
            calculator()
        else:
            should_continue = False


calculator()

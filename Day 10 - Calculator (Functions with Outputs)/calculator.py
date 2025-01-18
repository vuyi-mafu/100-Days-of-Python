from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}


def calculator():
    print(logo)

    continue_calc = True
    num1 = float(input("What is the first number?: "))

    while continue_calc:

        for operator in operations:
            print(operator)
        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What is the next number?: "))

        function = operations[operation_symbol]
        answer = function(n1=num1, n2=num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        calc_again = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. ").lower()

        if calc_again == "y":
            num1 = answer
        elif calc_again == "n":
            continue_calc = False
            calculator()


calculator()

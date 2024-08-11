def add(n1, n2):
    """Add two numbers."""
    return n1 + n2


def subtract(n1, n2):
    """Subtract two numbers."""
    return n1 - n2


def multiply(n1, n2):
    """Multiply two numbers."""
    return n1 * n2


def divide(n1, n2):
    """Divide two numbers. If the second number is 0, 0 will be returned."""
    if not n2 == 0:
        return n1 / n2
    else:
        return 0


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

first_number = None

while True:
    if first_number is None:
        first_number = float(input("Enter the first number: ]"))
        if first_number % 1 == 0:
            first_number = int(first_number)

    for symbol in operations:
        print(symbol)
    operand = input("Enter operation ]")

    second_number = float(input("Enter the second number: ]"))
    if second_number % 1 == 0:
        second_number = int(second_number)

    result = operations[operand](first_number, second_number)

    print(f"{first_number} {operand} {second_number} = {result}")

    go_again_with_result = input(f"Would you like to continue w/ {result} (Y/N)").upper()

    if go_again_with_result == 'Y':
        first_number = result
        second_number = None
    else:
        first_number = None
        second_number = None

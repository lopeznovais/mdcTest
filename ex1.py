def calculate(number1, number2, operator):
    if operator == '+':
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        if (number2 == 0):
            result = "Division by zero is invalid."
        else:
            result = number1 / number2

    return result


number1 = float(input("Enter the first number "))
number2 = float(input("Enter the second number "))
operator = input("Enter the operator ")

result = calculate(number1, number2, operator)

print(result)
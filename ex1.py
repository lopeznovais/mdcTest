def calculate(firstNumber, secondNumber, operator):
    if operator == '+':
        result = firstNumber + secondNumber
    elif operator == "-":
        result = firstNumber - secondNumber
    elif operator == "*":
        result = firstNumber * secondNumber
    elif operator == "/":
        if (secondNumber == 0):
            result = "Division by zero is invalid."
        else:
            result = firstNumber / secondNumber

    return result


firstNumber = float(input("Enter the first number "))
secondNumber = float(input("Enter the second number "))
operator = input("Enter the operator ")

result = calculate(firstNumber, secondNumber, operator)

print(result)
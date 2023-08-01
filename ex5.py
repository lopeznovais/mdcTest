def table(number):
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

number = int(input())
table(number)

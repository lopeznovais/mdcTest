def compound_interest(initialCapital, interestRate, timeInMonths):
    return initialCapital * (1 + interestRate/100) ** timeInMonths

initialCapital = float(input("Enter the initial capital: "))
interestRate = float(input("Enter the interest rate: "))
timeInMonths = int(input("Enter the investment time: "))

print(compound_interest(initialCapital,interestRate,timeInMonths))
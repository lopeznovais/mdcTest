def is_prime(number, i):
    if(number < 2):
        return False
    elif(number == i):
        return True
    elif(number % i == 0):
        return False

    return is_prime(number, i+1)

primeCounter = 0
number = 0
while(primeCounter < 10):
    if(is_prime(number, 2)):
        primeCounter += 1
        print(number)
    number += 1

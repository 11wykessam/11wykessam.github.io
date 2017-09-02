# challenge is to find the first triangular number to have over 500 divisors (including 5)

import math

def findDivisors(number) :
    divisors = []

    for n in range(1, int(math.sqrt(number))) :
        if number % n == 0:
            divisors.append(n)
            divisors.append(number / n)

    return divisors

def generateTriangularNumber(index) :
    sum = 0
    for n in range(1, index + 1) :
        sum += n

    return sum

number = 1
index = 1
while(True) :
    divisors = findDivisors(number)
    if index % 100 == 0:
        print(index)

    if len(divisors) > 500 :
        print(number)
        break

    index += 1
    number += index
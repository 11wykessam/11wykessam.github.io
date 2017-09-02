import math

def isPrime(a) :
    prime = True

    for i in range(2, int(math.sqrt(a) + 1)) :
        if a % i == 0 :
            prime = False

    return prime

def smallestprimefactor(a) :
    for i in range(2, a + 1) :
        if a % i == 0:
            if isPrime(i) :
                return i


def largestprimefactor(a) :
    while True :
        if isPrime(a) :
            print(a)
            break
        else :
            a = int(a / smallestprimefactor(a))

largestprimefactor(600851475143)
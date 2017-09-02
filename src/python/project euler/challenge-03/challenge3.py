# this challenge is to find the largest prime factor

import math

n = 600851475143

def isPrime(a) :
    prime = True

    for i in range(2, int(math.sqrt(a) + 1)) :
        if a % i == 0 :
            prime = False

    return prime


for i in range(int(math.sqrt(n) + 1), 0, -1):
    if isPrime(i) :
        if n % i == 0:
            print(i)
            break
    print(i)
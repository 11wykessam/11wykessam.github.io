#find nth prime numbers

def findPrimes(limit) :
    primes = []
    primes.append(2)
    pointer = 3
    while(len(primes) <= limit) :
        prime = True
        for i in primes :
            if pointer % i == 0:
                prime=False
                break

        if prime :
            primes.append(pointer)

        pointer += 1
    return primes

print(findPrimes(10001)[10000])
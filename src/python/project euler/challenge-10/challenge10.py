# this challenge is to find the sum of all primes below 2 million

def sum(numbers) :
    sum = 0
    for n in numbers:
        sum += int(n)
    return sum

primes = []


limit = 2000000

primebool = []

for n in range(limit) :
    primebool.append(True)

for n in range(2, limit) :
    if primebool[n] :
        i = 2 * n
        while i < limit :
            primebool[i] = False
            i += n

for n in range(limit) :
    if primebool[n] :
        primes.append(n)

print(sum(primes) - 1)
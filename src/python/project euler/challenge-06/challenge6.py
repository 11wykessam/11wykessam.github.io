#find the difference between the sum of the first 100 natural numbers squared and sum of the squares of the first 100 natural number

sumOfSquares = 0
sum = 0

for i in range(1, 101) :
    sum += i
    sumOfSquares += i**2

sum = sum**2

diff = sum - sumOfSquares

print(diff)

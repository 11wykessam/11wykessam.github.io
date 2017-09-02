# this challenge is to find the sum of multiples of 5 and 3 under 1000

n = 0

for i in range(1000) :
    if i % 3 == 0 or i % 5 == 0 :
        n += i

print(n)
# find the sum of the digits of 2^1000

n = str(2**1000)

sum = 0
for s in n :
    sum += int(s)

print(sum)

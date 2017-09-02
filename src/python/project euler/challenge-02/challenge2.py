# this challenge is sum of the fibonnaci numbers less than 4 million

#sum var
s = 0

# method to find nth fib number
def fib(n) :
    if n == 0 or n == 1:
        return 1
    else :
        return fib(n-1) + fib(n-2)


n = 0

while(fib(n) < 4000000) :
    currentValue = fib(n)
    if currentValue % 2 == 0:
        s += currentValue

    n += 1

print(s)
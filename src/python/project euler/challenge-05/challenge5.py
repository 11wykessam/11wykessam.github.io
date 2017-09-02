#find smallest integer that has the factors 1-20
n = 60

while(True) :
    correct = True
    for i in range(3, 21) :
        if n % i != 0:
            correct = False
            break
    if correct :
        print(n)
        break
    n += 60
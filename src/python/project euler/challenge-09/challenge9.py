#find the pythagorean triplet A, B, C such that A + B + C = 1000 then find the product

for a in range(1, 1000) :
    for b in range(a + 1, 1000 - a) :
        c = 1000 - a - b

        if a**2 + b**2 == c**2 :
            print("product = ", a*b*c)
            break

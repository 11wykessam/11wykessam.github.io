# find the sum of a massive amount of number

lines = []

sum = 0

with open("numbersToAdd.txt") as f :
    lines = f.readlines()
    lines = [line.strip("\n") for line in lines]

for s in lines :
    sum += int(s)

print(sum)
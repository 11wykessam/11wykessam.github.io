# find the longest collatz sequence that starts under a million
import sys

sys.setrecursionlimit(1000000)

foundValues = []

class pair :
    def __init__(self, index, value):
        self.index = index
        self.value = value


def isFound(index) :
    for p in foundValues :
        if p.index == index :
            return True

    return False

def getIndexValue(index) :
    for p in foundValues :
        if p.index == index :
            return p.value


def collatz(n, depth = 0) :
    depth += 1
    if n == 1 :
        return depth
    if n % 2 == 0 :
        return collatz(n / 2, depth)
    else :
        return collatz(3 * n + 1, depth)

maxValue = 0
answer = 0

for n in range(1, 1000001) :
    value = collatz(n)
    if value > maxValue :
        maxValue = value
        answer = n

print(answer)
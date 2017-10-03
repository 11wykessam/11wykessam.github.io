# this challenge is to find routes through a 20x20 lattice to the other corner
# to get to the bottom right of a x by y grid you need to take x right moves and y down moves

import math

def getNumberOfRoutes(x, y) :
    return math.factorial(x+y) / (math.factorial(x) * math.factorial(y))

print(getNumberOfRoutes(20 , 20))
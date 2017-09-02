#find the highest product of 4 adjacent numbers in a 20x20 grid

grid = []

lines = []

with open("grid.txt") as f :
    lines = f.readlines()
    lines = [line.strip("\n") for line in lines]

for line in lines :
    grid.append(line.split())

maximum = 0

#CONVERT TO INTS
for i in range(20) :
    for j in range(20) :
        grid[i][j] = int(grid[i][j])

# ROWS AND COLUMNS
for i in range(16) :
    for j in range(20) :
        rowTotal = 1
        columnTotal = 1

        for n in range(4) :
            rowTotal *= grid[i + n][j]
            columnTotal *= grid[j][i+n]

        if rowTotal > maximum :
            maximum = rowTotal

        if columnTotal > maximum :
            maximum = columnTotal

# DIAGONALS
for i in range(16) :
    for j in range(16) :
        diagLRTotal = 1
        diagRLTotal = 1
        for n in range(4) :
            diagLRTotal *= grid[i+n][j+n]
            diagRLTotal *= grid[i+4-n][j+n]

        if diagLRTotal > maximum:
            maximum = diagLRTotal

        if diagRLTotal > maximum :
            maximum = diagRLTotal

print(maximum)

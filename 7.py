import useful

file = useful.openFile(7)
grid = useful.createGrid(file)

values = {}
startPos = (0,0)
for val in grid.keys():
    if grid[val] == "^":
        if val[0] == 2:
            values[val] = True
        else:
            values[val] = False

    if grid[val] == "S":
        values[val] = True
        startPos = val

def determine(y,x):
    for i in range(y-1,-1,-1):
        if (i,x) in values.keys():
            return False
        if (i,x-1) in values.keys():
            if values[i,x-1] == True:
                values[y,x] = True
                return True
        if (i,x+1) in values.keys():
            if values[i,x+1] == True:
                values[y,x] = True
                return True

    return False
            
count = 0
for i in range(len(file)):
    for j in range(len(file[i])):
        if file[i][j] == "^":
            # print(values)
            # print((i,j), determine(i,j))
            if determine(i,j):
                count += 1

print(count+1)

memo = {}
def numPaths(y,x):
    out = 0
    if (y,x) in memo.keys():
        return memo[(y,x)]
    
    # -1
    found = False
    for i in range(y, len(file)):
        if grid[(i, x-1)] == "^":
            out += numPaths(i,x-1)
            found = True
            break
    if not found:
        out += 1
    # +1
    found = False
    for i in range(y, len(file)):
        if grid[(i, x+1)] == "^":
            out += numPaths(i,x+1)
            found = True
            break
    if not found:
        out += 1

    memo[(y,x)] = out
    return out

print(numPaths(2, startPos[1]))
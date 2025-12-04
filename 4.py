import useful

# print(useful.openFile(1))
file = useful.openFile(4)
grid = useful.createGrid(file)
for i in range(-1, len(file[0])+1):
    grid[(i,-1)] = "."
    grid[(-1,i)] = "."
    grid[(len(file[0]), i)] = "."
    grid[(i,len(file[0]))] = "."

def getNeighbors(x,y):
    out = []
    if grid[(x-1,y)] == "@":
        out.append((x-1,y))
    if grid[(x+1,y)] == "@":
        out.append((x+1,y))

    if grid[(x,y-1)] == "@":
        out.append((x,y-1))
    if grid[(x,y+1)] == "@":
        out.append((x,y+1))
    
    if grid[(x-1,y-1)] == "@":
        out.append((x-1,y-1))
    if grid[(x-1,y+1)] == "@":
        out.append((x-1,y+1))

    if grid[(x+1,y-1)] == "@":
        out.append((x+1,y-1))
    if grid[(x+1,y+1)] == "@":
        out.append((x+1,y+1))

    return out

total = 0
for i in range(len(file)):
    for j in range(len(file[0])):
        if len(getNeighbors(i,j)) < 4 and grid[(i,j)] == "@":
            total += 1

print(total)
removed = 0
done = False
def sthAccess():
    for i in range(len(file)):
        for j in range(len(file[0])):
            if len(getNeighbors(i,j)) < 4 and grid[(i,j)] == "@":
                return True
    return False

while True:
    if not sthAccess():
        break

    removeQ = []
    for i in range(len(file)):
        for j in range(len(file[0])):
            if len(getNeighbors(i,j)) < 4 and grid[(i,j)] == "@":
                removeQ.append((i,j))

    removed += len(removeQ)
    for i in removeQ:
        grid[i] = "."


print(removed)
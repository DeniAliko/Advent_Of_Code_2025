import useful
import queue
import numpy
from z3 import *
file = useful.openFile(10)

def getNeighbors(stri, buttons):
    out = []
    for button in buttons:
            c = str(stri[0])
            if isinstance(button, int):
                if c[button] == ".":
                    c = c[:button] + "#" + c[button+1:]
                else:
                    c = c[:button] + "." + c[button+1:]
            else:
                for toggle in button:
                    if c[toggle] == ".":
                        c = c[:toggle] + "#" + c[toggle+1:]
                    else:
                        c = c[:toggle] + "." + c[toggle+1:]

            out.append([str(c),stri[1]+1])
    # print(out)
    return out

formatted = []

for line in file:
    c = []
    c.append(line[1:line.find("]")])
    intervals = line.split(" ")[1:-1]
    b = []
    # print(intervals)
    for item in intervals:
        if "," not in item:
            b.append((int(item[1])))
        else:
            asdf = item.split(",")
            b.append(tuple([int(asdf[0][1:])] + [int(x) for x in asdf[1:-1]] + [int(asdf[-1][:-1])]))
    c.append(b)
    # print(c)

    formatted.append(c)

total = 0
for line in formatted:
    q = queue.Queue()
    goal = line[0]
    buttons = line[1]
    q.put(["."*len(goal),0])
    visited = []
    while not q.empty():
        current = q.get()
        neighbors = getNeighbors(current, buttons)
        breaks = False
        for neighbor in neighbors:
            if neighbor[0] == goal:
                # print(neighbor[1])
                total += neighbor[1]
                breaks = True
                break
            else:
                if neighbor not in visited:
                    visited.append(neighbor)
                    q.put(neighbor)

        if breaks:
            break

print(total)
formatted = []

for line in file:
    c = []
    aaa = [int(line.split(" ")[-1].split(",")[0][1:])] + [int(x) for x in line.split(" ")[-1].split(",")[1:-1]] + [int(line.split(" ")[-1].split(",")[-1][:-1])]
    c.append(aaa)
    intervals = line.split(" ")[1:-1]
    b = []
    # print(intervals)
    for item in intervals:
        if "," not in item:
            b.append((int(item[1])))
        else:
            asdf = item.split(",")
            b.append(tuple([int(asdf[0][1:])] + [int(x) for x in asdf[1:-1]] + [int(asdf[-1][:-1])]))
    c.append(b)
    # print(c)

    formatted.append(c)

total = 0
for line in formatted:
    b = numpy.array(line[0])
    buttons = line[1]
    a = []
    for button in buttons:
        
        c = [0 for i in range(len(b))]
        if isinstance(button, int):
            c[button] = 1
        else:
            for butto in button:
                c[butto] = 1

        a.append(c)

    aa = numpy.vstack((numpy.array(a), b)).T

    # print(aa)
    s = Optimize()

    vars = [Int(f"x{i}") for i in range(len(aa[0])-1)]
    for var in vars:
        s.add(var >= 0)
    for line in aa:
        coeffs = [g for g in line[:-1]]
        s.add(sum([vars[i]*coeffs[i] for i in range(len(aa[0])-1)]) == line[-1])

    
    s.minimize(sum(vars))
    # print(s.check())
    if s.check() == sat:
        m = s.model()
        print(s.model())
        for d in m.decls():
            total += m[d].as_long()

        # total += numpy.linalg.norm(solVec, ord = 1)

print(total)
import useful

file = useful.openFile(8)

def N(a,b):
    out = 0
    for i in range(3):
        out += (a[i] - b[i])**2
    return out

pts = []
for line in file:
    pts.append(tuple([int(i) for i in line.split(",")]))

dists1 = {}
for i in range(len(pts)):
    for j in range(i+1,len(pts)):
        dists1[(tuple(pts[i]),tuple(pts[j]))] = N(pts[i],pts[j])

dists = {k: v for k, v in sorted(dists1.items(), key=lambda item: item[1])}
cycles = []

for index in range(1000):
    minKey = next(iter(dists))
    minDist = dists[minKey]

    a = minKey[0]
    b = minKey[1]

    # searching for them in the cycles
    found = False
    aIn = False
    aindex = None
    bIn = False
    bindex = None
    for i in range(len(cycles)):
        if a in cycles[i]:
            found = True
            aIn = True
            aindex = i
        if b in cycles[i]:
            found = True
            bIn = True
            bindex = i

    # neither in any
    if not found:
        cycles.append([a,b])
    # both in one
    if aIn and bIn:
        if aindex == bindex:
            del dists[minKey]
            # if index % 10 == 0:
            #     print("Found:", index)
            continue
    # both in different ones
    if aIn and bIn:
        if aindex != bindex:
            for item in cycles[bindex]:
                cycles[aindex].append(item)
            cycles.pop(bindex)
    # one in one, other in none
    if aIn and not bIn:
        cycles[aindex].append(b)
    if bIn and not aIn:
        cycles[bindex].append(a)

    del dists[minKey]
    # if index % 10 == 0:
    #     print("Found:", index)

# print(cycles)
sortLengths = [len(i) for i in cycles]
sortLengths.sort()
sortLengths.reverse()
print(sortLengths[0],sortLengths[1],sortLengths[2])
print(sortLengths[0]*sortLengths[1]*sortLengths[2])

dists = {k: v for k, v in sorted(dists1.items(), key=lambda item: item[1])}
cycles = [[]]

goLong = True
count = 0
while len(cycles[0]) != len(file):
    if count == 0:
        cycles = []
    minKey = next(iter(dists))
    minDist = dists[minKey]
    count += 1
    print(count)
    # print(cycles)

    a = minKey[0]
    b = minKey[1]

    # searching for them in the cycles
    found = False
    aIn = False
    aindex = None
    bIn = False
    bindex = None
    for i in range(len(cycles)):
        if a in cycles[i]:
            found = True
            aIn = True
            aindex = i
        if b in cycles[i]:
            found = True
            bIn = True
            bindex = i

    # neither in any
    if not found:
        cycles.append([a,b])
    # both in one
    if aIn and bIn:
        if aindex == bindex:
            del dists[minKey]
            # if index % 10 == 0:
            #     print("Found:", index)
            continue
    # both in different ones
    if aIn and bIn:
        if aindex != bindex:
            for item in cycles[bindex]:
                cycles[aindex].append(item)
            cycles.pop(bindex)
    # one in one, other in none
    if aIn and not bIn:
        cycles[aindex].append(b)
    if bIn and not aIn:
        cycles[bindex].append(a)

    del dists[minKey]
    # if index % 10 == 0:
    #     print("Found:", index)

print(minKey)
print(minKey[0][0]*minKey[1][0])
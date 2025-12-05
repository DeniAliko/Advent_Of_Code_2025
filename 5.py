import useful
import queue

file = useful.openFile(5)

ranges = []
ids = []
out = 0
idCheck = False
for line in file:
    if idCheck:
        ids.append(int(line))
        continue

    if line == "":
        idCheck = True
        continue

    ranges.append((int(line.split("-")[0]),int(line.split("-")[1])))

# print(ranges)
# print(ids)
for item in ids:
    good = False
    for rrange in ranges:
        if item <= rrange[1] and item >= rrange[0]:
            good = True
            continue

    if good:
        out += 1
print(out)

# def compactify(inp):
#     output = [inp[0]]
#     for rrange in inp[1:]:

#         subset = False

#         intersected = False
#         if not subset:
#             for asd in output:
#                 if rrange[0] <= asd[0] <= rrange[1]:
#                     asd[0] = rrange[0]
#                     intersected = True
#                     output = compactify(output)

#                 if rrange[1] >= asd[1] >= rrange[0]:
#                     asd[1] = rrange[1]
#                     intersected = True
#                     output = compactify(output)

#         if not intersected:
#             output.append(list(rrange))
            

#     return output

# IDEA: sort the list
findices = {}
for range in ranges:
    if range[0] not in findices.keys():
        findices[range[0]] = list(range)

    else:
        if range[1] > findices[range[0]][1]:
            findices[range[0]] = list(range)


sort = sorted(findices.keys())
print(sort)
sortedIntervals = []
for i in sort:
    sortedIntervals.append(findices[i])

merged = [sortedIntervals[0]]
for interval in sortedIntervals[1:]:
    if interval[0] > merged[-1][1]:
        merged.append(interval)
    elif merged[-1][0] <= interval[0] <= merged[-1][1] and merged[-1][0] <= interval[1] <= merged[-1][1]:
        continue
    else:
        merged[-1][1] = interval[1]

final = 0
for i in merged:
    final += i[1]-i[0]+1
# print(merged)
print(final)

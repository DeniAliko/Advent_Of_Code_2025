import useful

file = useful.openFile(9)
pts = []
for line in file:
    pts.append([int(i) for i in line.split(",")])

max = 0
for i in range(len(pts)):
    for j in range(len(pts)):
        if (abs(pts[i][0]-pts[j][0]) + 1)*(abs(pts[i][1]-pts[j][1]) + 1) > max:
            max = (abs(pts[i][0]-pts[j][0]) + 1)*(abs(pts[i][1]-pts[j][1]) + 1)

print(max)
print([tuple(i) for i in pts])

# y cutoff: 49140
# key pts: (94918,50338),(94918,48430)
# https://www.desmos.com/calculator/mdgzst8ykd

max = 0
for i in range(len(pts)):
    if pts[i][1] > 49140:
        possible = True
        for pt in pts:
            if pts[i][0] < pt[0] < 94918 and 50338 < pt[1] < pts[i][1]:
                possible = False

        if possible and (abs(pts[i][0]-94918) + 1)*(abs(pts[i][1]-50338) + 1) > max:
            max = (abs(pts[i][0]-94918) + 1)*(abs(pts[i][1]-50338) + 1)
    else:
        possible = True
        for pt in pts:
            if pts[i][0] < pt[0] < 94918 and pts[i][1] < pt[1] < 48430:
                possible = False
        if possible and (abs(pts[i][0]-94918) + 1)*(abs(pts[i][1]-48430) + 1) > max:
            max = (abs(pts[i][0]-94918) + 1)*(abs(pts[i][1]-48430) + 1)

print(max)
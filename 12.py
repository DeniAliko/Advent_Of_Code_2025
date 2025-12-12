import useful

file = useful.openFile(12)

lines = []
for line in file:
    c = []
    c.append([int(i) for i in line.split(":")[0].split("x")])
    c.append([int(i) for i in line.split(":")[1].split(" ")[1:]])
    lines.append(c)
    # print(c)

# real
p0 = useful.createGrid(["##.",".##", "..#"])
p1 = useful.createGrid(["###",".##", "##."])
p2 = useful.createGrid(["#.#","###", "#.#"])
p3 = useful.createGrid(["###","#..", "###"])
p4 = useful.createGrid(["###","###", "..#"])
p5 = useful.createGrid(["###","##.", "#.."])

# test
# p0 = useful.createGrid(["###","##.", "##."])
# p1 = useful.createGrid(["###","##.", ".##"])
# p2 = useful.createGrid([".##","###", "##."])
# p3 = useful.createGrid(["##.","###", "##."])
# p4 = useful.createGrid(["###","#..", "###"])
# p5 = useful.createGrid(["###",".#.", "###"])

for i in [p0,p1,p2,p3,p4,p5]:
    for j in i.keys():
        if i[j] == "#":
            i[j] = True
        else:
            i[j] = False

total = 0
for line in lines:
    threebythrees = (line[0][0] // 3) * (line[0][1] // 3)
    if threebythrees >= sum(line[1]):
        total += 1
        print("GOOD:", line)
print(total)
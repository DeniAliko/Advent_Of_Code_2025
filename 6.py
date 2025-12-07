import useful

file1 = open("6.txt")
file = []
linesInFile = file1.readlines()
for i in linesInFile:
    file.append(format(i.rstrip()))

inp = []
for i in range(0,len(file)-1):
    c = [j for j in file[i].split(" ")]
    cc = []
    for j in c:
        if j != "":
            cc.append(int(j))

    inp.append(cc)

c = file[-1].split(" ")
cc = []
for j in c:
    if j != "":
        cc.append(j)
inp.append(cc)

out = 0
for i in range(0, len(inp[0])):
    if inp[-1][i] == "+":
        c = 0
        for j in range(len(inp)-1):
            c += inp[j][i]

        out += c

    elif inp[-1][i] == "*":
        c = 1
        for j in range(len(inp)-1):
            c *= inp[j][i]   

        out += c    

print(out)

newFile = []
maxLength = max([len(i) for i in file])
for line in file:
    c = []
    for char in line:
        c.append(char)
    while len(c) < maxLength+1:
        c.append(" ")

    newFile.append(c)

secs = []
cache = ["","","","",""]
for i in range(maxLength):
    
    if newFile[0][i] == newFile[1][i] == newFile[2][i] == newFile[3][i] == newFile[4][i] == " ":
        secs.append(cache)
        cache = ["","","","",""]
    else:
        cache[0] += newFile[0][i]
        cache[1] += newFile[1][i]
        cache[2] += newFile[2][i]
        cache[3] += newFile[3][i]
        cache[4] += newFile[4][i]
secs.append(cache)
for item in secs:
    numlength = len(item[0])
    for i in item[:-1]:
        if i[-1] == " ":
            c = i.rstrip()
            while len(c) < numlength:
                c += "0"

            i = c


for item in secs:
    item[4] = item[4].strip()

print(secs)

out = 0
for item in secs:
    numlength = len(item[0])
    if item[4] == "+":
        a = 0
        b = 0
        c = 0
        d = 0

    else:
        a = 1
        b = 1
        c = 1
        d = 1


    if numlength == 4:
        a = int(item[0][0] + item[1][0] + item[2][0] + item[3][0])
        b = int(item[0][1] + item[1][1] + item[2][1] + item[3][1])
        c = int(item[0][2] + item[1][2] + item[2][2] + item[3][2])
        d = int(item[0][3] + item[1][3] + item[2][3] + item[3][3])

    if numlength == 3:
        a = int(item[0][0] + item[1][0] + item[2][0] + item[3][0])
        b = int(item[0][1] + item[1][1] + item[2][1] + item[3][1])
        c = int(item[0][2] + item[1][2] + item[2][2] + item[3][2])


    if numlength == 2:
        a = int(item[0][0] + item[1][0] + item[2][0] + item[3][0])
        b = int(item[0][1] + item[1][1] + item[2][1] + item[3][1])



    if item[4] == "+":
        # print(item, a+b+c+d)
        out += a+b+c+d
    elif item[4] == "*":
        # print(item, a*b*c*d)
        out += a*b*c*d
    
print(out)
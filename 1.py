import useful

# print(useful.openFile(1))
file = useful.openFile(1)
pos = 50
ct = 0
for line in file:
    if line[0] == "L":
        pos -= int(line[1:])
    else:
        pos += int(line[1:])
    if pos % 100 == 0:
        ct += 1
    # print(pos)

print(ct)

ct = 0
pos = 50
for line in file:
    if line[0] == "L":
        for i in range(int(line[1:])):
            pos -= 1
            # print(pos)
            if pos % 100 == 0:
                ct += 1
    else:
        for i in range(int(line[1:])):
            pos += 1
            # print(pos)
            if pos % 100 == 0:
                ct += 1

print(ct)
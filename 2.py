import useful

# print(useful.openFile(1))
file = useful.openFile(2)
ids = file[0].split(",")
# print(ids)
cct = 0
for pair in ids:
    for i in range(int(pair.split("-")[0]), int(pair.split("-")[1])+1):
        if len(str(i)) % 2 == 0:
            if int(str(i)[:int(len(str(i))/2)]) == int(str(i)[int(len(str(i))/2):]):
                cct += i

print(cct)
cct = 0
found = {}
for pair in ids:
    found[pair] = []
    for i in range(int(pair.split("-")[0]), int(pair.split("-")[1])+1):
        for j in range(1,len(str(i))):
            good = True
            for item in str(i).split(str(i)[:j]):
                if item != "":
                    good = False

            if good and i not in found[pair]:
                cct += i
                found[pair].append(i)

print(cct)

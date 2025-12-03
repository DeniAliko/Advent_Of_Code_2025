import useful

# print(useful.openFile(1))
file = useful.openFile(3)
sum = 0
for line in file:
    current = 0
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            if int(line[i]+line[j]) > current:
                current = int(line[i]+line[j])

    sum += current

print(sum)

def findBiggest(num, length):
    if length == 0:
        return ""
    if length == 1:
        for i in range(9,-1,-1):
            if str(i) in list(num):
                return str(i)
    for i in range(9,-1,-1):
        if str(i) in list(num)[:-length+1]:
            return str(i) + str(findBiggest(num[list(num).index(str(i))+1:], length - 1))
        
sum = 0
for line in file:
    c = int(findBiggest(line, 12))
    sum += c
    # print(c)
    
# print(findBiggest("234234234234278", 12))
print(sum)
# 3121910778619
# 3110379966860
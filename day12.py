file = open("input12test.txt", "r")
lines = [line.replace("\n","") for line in file.readlines()]

for i in range(0, len(lines)):
    lines[i] = lines[i].split(" ")
    lines[i][1] = lines[i][1].split(",")
for i in range(0, len(lines)):
    for j in range(0, len(lines[i][1])):
        lines[i][1][j] = int(lines[i][1][j])
        
def getArrangements(line):
    arrangements = 0
    index = 0
    record = 0
    while index != len(line[0]):
        while line[0][index] == '.':
            index += 1
        
        if line[0][index:index+line[1][record]] == line[1][record]*'#':
            index += line[1][record]
            record += 1

        if line[0][index:index+line[1][record]] == line[1][record]*'?':
            index += line[1][record]
            record += 1
        else:
            unknown = 1
            while line[0][index] == '?':
                unknown += 1
            arrangements += 2
            
def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def binom(n, k):
    return fact(n) / (fact(k) * fact(n-k))

print(binom(5, 2))
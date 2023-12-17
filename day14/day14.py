file = open("input14test.txt", "r")
lines = file.read().strip("\n")
lines = lines.split("\n")

N = len(lines)
M = len(lines[0])

def getRockNorth(array, i, j):
    res = True
    while j < N and array[j][i] != 'O':
        j += 1
    if j == N:
        res = False
    return j, res

def moveRockNorth(array, i, j):
    k = j
    while k > 0 and array[k-1][i] == '.':
        l = list(array[k-1])
        l[i] = 'O'
        array[k-1] = "".join(l)
        l = list(array[k])
        l[i] = '.'
        array[k] = "".join(l)
        k -= 1
    return array
        
def tiltNorth(array):
    for i in range(M):
        j = 0
        while j < N:
            j, mr= getRockNorth(array, i, j)
            if mr:
                array = moveRockNorth(array, i, j)
            j += 1
    return array
            
def getRockSouth(array, i, j):
    res = True
    while j > -1 and array[j][i] != 'O':
        j -= 1
    if j == -1:
        res = False
    return j, res

def moveRockSouth(array, i, j):
    k = j
    while k < N-1 and array[k+1][i] == '.':
        l = list(array[k+1])
        l[i] = 'O'
        array[k+1] = "".join(l)
        l = list(array[k])
        l[i] = '.'
        array[k] = "".join(l)
        k += 1
    return array
     
def tiltSouth(array):
    for i in range(M):
        j = M-1
        while j > -1:
            j, mr = getRockSouth(array, i, j)
            if mr:
                array = moveRockSouth(array, i, j)
            j -= 1
    return array

def getRockEast(array, i, j):
    res = True
    while j > -1 and array[i][j] != 'O':
        j -= 1
    if j == -1:
        res = False
    return j, res

def moveRockEast(array, i, j):
    k = j
    while k < M-1 and array[i][k+1] == '.':
        l = list(array[i])
        l[k+1] = 'O'
        array[i] = "".join(l)
        l = list(array[i])
        l[k] = '.'
        array[i] = "".join(l)
        k += 1
    return array
        
def tiltEast(array):
    for i in range(N):
        j = M-1
        while j > -1:
            j, mr= getRockEast(array, i, j)
            if mr:
                array = moveRockEast(array, i, j)
            j -= 1
    return array

def getRockWest(array, i, j):
    res = True
    while j < M and array[i][j] != 'O':
        j += 1
    if j == M:
        res = False
    return j, res

def moveRockWest(array, i, j):
    k = j
    while k > 0 and array[i][k-1] == '.':
        l = list(array[i])
        l[k-1] = 'O'
        array[i] = "".join(l)
        l = list(array[i])
        l[k] = '.'
        array[i] = "".join(l)
        k -= 1
    return array
        
def tiltWest(array):
    for i in range(N):
        j = 0
        while j < M:
            j, mr = getRockWest(array, i, j)
            if mr:
                array = moveRockWest(array, i, j)
            j += 1
    return array

cycletable = []     
for i in range(3):
    lines = tiltNorth(lines)
    lines = tiltWest(lines)
    lines = tiltSouth(lines)
    lines = tiltEast(lines)
    cycletable.append(lines)
    

st = 0
l = N
for line in lines:
    s = 0
    for ch in line:
        if ch == 'O':
            s += 1
    st += N * s
    N -= 1

print(st)

i = 1
tab = cycletable[0]
while cycletable[i] != tab:
    i += 1

print(i)
import numpy as np
file = open("input11.txt", "r")
universe = file.read().split("\n")

N = 999999

def expandUniverse(universe, nbline, nbcolumn):
    expandedUniverse = universe

    offset = 0
    for i in range(0, nbcolumn):
        column = getColumn(expandedUniverse, offset)
        if '#' not in column:
            for i in range(0, nbline):
                expandedUniverse[i] = expandedUniverse[i][:offset] + N * '.' + expandedUniverse[i][offset:]
            nbcolumn += N
            offset += N
        offset += 1

    offset = 0
    for line in expandedUniverse:
        if '#' not in line:
            expandedUniverse = expandedUniverse[:offset] + N * [nbcolumn * '.'] + expandedUniverse[offset:]
            nbline += N
            offset += N
        offset += 1

    return expandedUniverse

# Extracts column from array
def getColumn(array, i):
    return [row[i] for row in array]

class Matrice:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def distance(self, matrice):
        return abs(matrice.x - self.x) + abs(matrice.y - self.y)
    
expandedUniverse = expandUniverse(universe, len(universe[0]), len(universe[0]))

def getAllIndex(array, value):
    indexs = []
    offset = 0
    while (value in array[offset:]):
        offset += array[offset:].index(value) + 1
        indexs.append(offset-1)
    return indexs

galaxies = []
i = 0
for ligne in expandedUniverse:
    if '#' in ligne:
        indexs = getAllIndex(ligne, '#')
        for k in indexs:
            galaxies.append(Matrice(i, k))
    i += 1

s = 0
for i in range(0, len(galaxies)-1):
    for j in range(i+1, len(galaxies)):
        s += galaxies[i].distance(galaxies[j])

print(s)
        
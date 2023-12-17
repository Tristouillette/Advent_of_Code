file = open("input16.txt", "r")
contraption = file.read().strip("\n")
contraption = contraption.split("\n")

# Get rid of \n
for i in range(len(contraption)-1):
    contraption[i] = contraption[i][0:len(contraption[i])]

# Add ? before and after each line
for i in range(len(contraption)):
    contraption[i] = '?' + contraption[i] + '?'
# Add line of ? at the end
contraption.append(len(contraption[0])*'?')
# Add line of ? at the beginning
c = [(len(contraption[0]))*'?']
for i in range(len(contraption)):
    c.append(contraption[i])

# Contraption done
contraption = c

# DEFINE MAP
MAP = []
def loadMap(N = 112):
    MAP = []
    for i in range(N):
        MAP.append([0])
        for j in range(N-1):
            MAP[i].append(0)
    return MAP
#  -----> y
# |
# |
# v
# x

class Matrice:
    def __init__(self, x, y, form, isfrom):
        self.x = x
        self.y = y
        self.form = form
        self.isfrom = isfrom
        
    def __str__(self):
        return f"({self.x}, {self.y}, {self.form}, {self.isfrom})"

    def __next__(self):
        if self.form == '.':
            if   self.isfrom == 'w': self.y += 1
            elif self.isfrom == 'e': self.y -= 1
            elif self.isfrom == 'n': self.x += 1
            elif self.isfrom == 's': self.x -= 1

        elif self.form == '/':
            if   self.isfrom == 'w': 
                self.x -= 1 
                self.isfrom = 's'
            elif self.isfrom == 'e': 
                self.x += 1
                self.isfrom = 'n'
            elif self.isfrom == 'n': 
                self.y -= 1
                self.isfrom = 'e'
            elif self.isfrom == 's': 
                self.y += 1
                self.isfrom = 'w'

        elif self.form == '\\':
            if   self.isfrom == 'w': 
                self.x += 1
                self.isfrom = 'n'
            elif self.isfrom == 'e': 
                self.x -= 1
                self.isfrom = 's'
            elif self.isfrom == 'n': 
                self.y += 1
                self.isfrom = 'w'
            elif self.isfrom == 's': 
                self.y -= 1
                self.isfrom = 'e'

        elif self.form == '-':
            if   self.isfrom == 'w': self.y += 1
            elif self.isfrom == 'e': self.y -= 1
            elif self.isfrom == 's' or self.isfrom == 'n':
                if MAP[self.x][self.y] >= 2:
                    self.form = '?'
                    return self
                cloneBeam = Matrice(self.x, self.y, self.form, self.isfrom)
                cloneBeam.form = contraption[cloneBeam.x][cloneBeam.y]
                cloneBeam.isfrom = 'w'
                launchBeam(cloneBeam) # This one goes right
                self.y -= 1 # This one goes left
                self.isfrom = 'e'
                
        elif self.form == '|':
            if   self.isfrom == 's': self.x -= 1
            elif self.isfrom == 'n': self.x += 1
            elif self.isfrom == 'w' or self.isfrom == 'e':
                if MAP[self.x][self.y] >= 2:
                    self.form = '?'
                    return self
                cloneBeam = Matrice(self.x, self.y, self.form, self.isfrom)
                cloneBeam.form = contraption[cloneBeam.x][cloneBeam.y]
                cloneBeam.isfrom = 'n'
                launchBeam(cloneBeam) # This one goes down
                self.x -= 1 # This one goes up
                self.isfrom = 's'
        
        self.form = contraption[self.x][self.y]
        MAP[self.x][self.y] += 1
        return self

def launchBeam(beam):
    while beam.form != '?' or MAP[beam.x][beam.y] < 2:
        beam = beam.__next__()

# MAX
stot = 0

# LAUNCH FROM WEST
for i in range(1, len(contraption)-1):
    MAP = loadMap()
    firstBeam = Matrice(i, 1, contraption[i][1], 'w')
    MAP[i][1] = 1
    launchBeam(firstBeam)
    sw = 0
    for i in range(1, len(MAP)-1):
        for j in range(1, len(MAP)-1):
            if MAP[i][j] != 0:
                sw += 1
    if sw > stot:
        stot = sw

# LAUNCH FROM EAST
for i in range(1, len(contraption)-1):
    MAP = loadMap()
    firstBeam = Matrice(i, len(contraption)-2, contraption[i][len(contraption)-2], 'e')
    MAP[i][len(contraption)-2] = 1
    launchBeam(firstBeam)
    ss = 0
    for i in range(1, len(MAP)-1):
        for j in range(1, len(MAP)-1):
            if MAP[i][j] != 0:
                ss += 1
    if ss > stot:
        stot = ss

# LAUNCH FROM NORTH
for i in range(1, len(contraption)-1):
    MAP = loadMap()
    firstBeam = Matrice(1, i, contraption[1][i], 'n')
    MAP[1][i] = 1
    launchBeam(firstBeam)
    se = 0
    for i in range(1, len(MAP)-1):
        for j in range(1, len(MAP)-1):
            if MAP[i][j] != 0:
                se += 1
    if se > stot:
        stot = se

# LAUNCH FROM SOUTH
for i in range(1, len(contraption)-1):
    MAP = loadMap()
    firstBeam = Matrice(len(contraption)-2, i, contraption[len(contraption)-2][i], 's')
    MAP[len(contraption)-1][i] = 1
    launchBeam(firstBeam)
    sn = 0
    for i in range(1, len(MAP)-1):
        for j in range(1, len(MAP)-1):
            if MAP[i][j] != 0:
                sn += 1
    if sn > stot:
        stot = sn

print(stot)
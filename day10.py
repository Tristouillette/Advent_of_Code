file = open("input10.txt", "r")
contenu = file.read().split("\n")

# Character and Status
pipes = {"|": "ns", 
         "-": "ew",
         "L": "ne",
         "J": "nw",
         "7": "sw",
         "F": "se",
         ".": ""  ,
         "S": "se"}

# Returns the opposite direction
def reverse(char):
    if char == 'n': return 's'
    if char == 's': return 'n'
    if char == 'e': return 'w'
    if char == 'w': return 'e'

class Matrice:
    def __init__(self, x, y, pipe, status):
        self.x = x
        self.y = y
        self.pipe = pipe
        self.status = status
        
    def __str__(self):
        return f"({self.x}, {self.y}, {self.pipe}, {self.status})"
    
    # initialisation of the two walkers
    def __initWalkers__(self):
        east = Matrice(self.x, self.y + 1, contenu[self.x][self.y + 1], pipes[contenu[self.x][self.y + 1]].replace('w',''))
        north = Matrice(self.x - 1, self.y, contenu[self.x - 1][self.y], pipes[contenu[self.x - 1][self.y]].replace('s',''))
        return east, north

    def __next__(self):
        if   self.status == 'n': self.x -= 1
        elif self.status == 's': self.x += 1
        elif self.status == 'w': self.y -= 1
        elif self.status == 'e': self.y += 1
        self.pipe = contenu[self.x][self.y]
        self.status = pipes[self.pipe].replace(reverse(self.status), '')
        return self

    def getPosition(self):
        return (self.x, self.y)
    
    def getPipe(self):
        return self.pipe

# Get the Start position
for i in range(0, len(contenu)):
    for j in range(0, len(contenu[i])):
        if contenu[i][j] == 'S':
            S = Matrice(i, j, 'S', pipes['S'])
            break
# Initialize Walkers
walker1, walker2 = S.__initWalkers__()

i = 1
while walker1.getPosition() != walker2.getPosition():
    i += 1
    walker1.__next__()
    walker2.__next__()
print(i)
    
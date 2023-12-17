import time
fichier = open('input1.txt', 'r')
contenu = fichier.readlines()

def isNumber(n, ligne, offset):
    if ord(n) >= 49 and ord(n) <= 57:
        return int(n)
    
    if n == 'o':
        if ligne[offset+1:offset+3] == "ne":
            return 1        
    elif n == 't':
        if ligne[offset+1:offset+3] == "wo":
            return 2
        if ligne[offset+1:offset+5] == "hree":
            return 3    
    elif n == 'f':
        if ligne[offset+1:offset+4] == "our":
            return 4
        if ligne[offset+1:offset+4] == "ive":
            return 5    
    elif n == 's':
        if ligne[offset+1:offset+3] == "ix":
            return 6
        if ligne[offset+1:offset+5] == "even":
            return 7    
    elif n == 'e':
        if ligne[offset+1:offset+5] == "ight":
            return 8    
    elif n == 'n':
        if ligne[offset+1:offset+4] == "ine":
            return 9    
    return False

def isNumber2(n, ligne, offset):
    if ord(n) >= 49 and ord(n) <= 57:
        return int(n)
    
    if n == 'e':
        if ligne[offset-3:offset-1] == "on":
            return 1 
        if ligne[offset-5:offset-1] == "thre":
            return 3
        if ligne[offset-4:offset-1] == "fiv":
            return 5 
        if ligne[offset-4:offset-1] == "nin":
            return 9        
    elif n == 'o':
        if ligne[offset-3:offset-1] == "tw":
            return 2
    elif n == 'r':
        if ligne[offset-4:offset-1] == "fou":
            return 4
    elif n == 'x':
        if ligne[offset-3:offset-1] == "si":
            return 6
    elif n == 'n':
        if ligne[offset-5:offset-1] == "seve":
            return 7    
    elif n == 't':
        if ligne[offset-5:offset-1] == "eigh":
            return 8    
    return False

def computeCalibrationValue(ligne):
    offset = 0
    for character in ligne:
        first = isNumber(character, ligne, offset)
        if first != False:
            break
        offset += 1

    offset = len(ligne) 
    for character in ligne[::-1]:
        second = isNumber2(character, ligne, offset)
        if second != False:
            break
        offset -= 1

    return int(str(first) + str(second))

t1 = time.time()
s = 0
for ligne in contenu:
    s += computeCalibrationValue(ligne.strip())
t2 = time.time()
print(s)
print(t2-t1)


fichier.close()
file = open("input13.txt", "r")
allpatterns = file.read().split("\n\n")
patterns = [pattern for pattern in allpatterns]

row = ""
allpatternsarray = []
for i in range(0, len(patterns)):
    patternsarray = []
    for pattern in patterns[i].split("\n"):
        patternsarray.append(pattern)
    allpatternsarray.append(patternsarray)

def findVerticalReflection(pattern):
    for l in range(0, len(pattern)):
        for i in range(0, len(pattern[l])):
            for j in range(i+2, len(pattern[l])+1):
                if pattern[l][i:j] == pattern[l][i:j][::-1]:
                    f = True    
                    for nl in range(l+1, len(pattern)):
                        if pattern[nl][i:j] != pattern[nl][i:j][::-1]:
                            f = False
                            break 
                    if f:
                        return (i + j) // 2
        return 0
                    
#print(findVerticalReflection(allpatternsarray[0]))

def findHorizontalReflection(pattern):
    n = len(pattern[0])
    for l in range(0, len(pattern)-1):
        if pattern[l] == pattern[l+1]:
            i = l-1
            j = l+2
            f = True
            while i >= 0 and j <= len(pattern)-1:
                if pattern[i] != pattern[j]:
                    f = False
                    break
                i -= 1
                j += 1
            if f:
                return 100 * ((i + j + 1) // 2)
    return 0
                
#print(findHorizontalReflection(allpatternsarray[1]))

s = 0
i = 0
for pattern in allpatternsarray:
    v = findVerticalReflection(pattern)
    h = findHorizontalReflection(pattern)
    #print(v, h)
    s += v
    s += h
    i += 1
    
print(s)
    
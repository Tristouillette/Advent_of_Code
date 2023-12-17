fichier = open('input9.txt', 'r')
lines = fichier.readlines()

lines = [lines[i].replace("\n", "").split(" ") for i in range(0, len(lines))]
for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        lines[i][j] = int(lines[i][j])
    
def extrapolate(history):
    sequences = [history]
    offset = 0
    while True:
        subsequence = []
        for i in range(0, len(sequences[offset])-1):
            subsequence.append(sequences[offset][i+1] - sequences[offset][i])
        if subsequence == len(subsequence)*[0]:
            break
        sequences.append(subsequence)
        offset += 1

    values = []
    for i in range(0, len(sequences)):
        values.append(sequences[i][0])
    values = values[::-1]

    a = 0
    b = values[0]
    for i in range(1, len(values)):
        a = b - a
        b = values[i]

    return b - a

s = 0
for i in lines:
    s += extrapolate(i)

print(s)

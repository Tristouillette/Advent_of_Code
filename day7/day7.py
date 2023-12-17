fichier = open('input7.txt', 'r')
contenu = fichier.readlines()

# Card values
value = {r:i for i,r in enumerate('23456789TJQKA', 2)}

# Type strengths
Five_of_a_kind  = 6
Four_of_a_kind  = 5
Full_house      = 4
Three_of_a_kind = 3
Two_pair        = 2
One_pair        = 1
Nothing         = 0

def getType(hand):
    sh = sorted(hand)
    if sh[0:5] == sh[0:5][::-1]:
        return Five_of_a_kind
    if sh[0:4] == sh[0:4][::-1] or sh[1:5] == sh[1:5][::-1]:
        return Four_of_a_kind
    if (sh[0:3] == sh[0:3][::-1] and sh[3:5] == sh[3:5][::-1]) or (sh[2:5] == sh[2:5][::-1] and sh[0:2] == sh[0:2][::-1]):
        return Full_house
    if sh[0:3] == sh[0:3][::-1] or sh[1:4] == sh[1:4][::-1] or sh[2:5] == sh[2:5][::-1]:
        return Three_of_a_kind
    p = 0
    for i in range(0, 4):
        if sh[i:i+2] == sh[i:i+2][::-1]:
            p += 1
    if p == 2:
        return Two_pair
    if p == 1:
        return One_pair
    return Nothing

# True : hand1 is stronger
def compare(hand1, hand2):
    if hand1[2] > hand2[2]:
        return True
    if hand1[2] < hand2[2]:
        return False
    for i in range(0, 5):
        if value[hand1[0][i]] > value[hand2[0][i]]:
            return True
        if value[hand1[0][i]] < value[hand2[0][i]]:
            return False

Hands = []
it = 0
for hand in contenu:
    Hands.append(hand.strip().split(" "))
    Hands[it].append(getType(hand.strip().split(" ")[0]))
    it += 1

def tri_bulle(h):
    for i in range(len(h)):
        for j in range(0, len(h)-i-1):
            if compare(h[j], h[j+1]):
                h[j], h[j+1] = h[j+1], h[j]

tri_bulle(Hands)

s = 0
m = 1
for hand in Hands:
    s += int(hand[1]) * m
    m += 1

print(s)

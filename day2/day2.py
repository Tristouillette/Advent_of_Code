fichier = open('input2.txt', 'r')
contenu = fichier.readlines()    

s = 0
id = 0
for ligne in contenu:
    colors = {"red": 0, "green": 0, "blue": 0}
    condition = True
    id += 1
    if id >= 10:
        step = len(str(id//10))
    else:
        step = 0
    for i in ligne.strip()[7 + step : len(ligne)].split(";"):
        for j in i.split(","):
            if int(j.split(" ")[1]) > colors[j.split(" ")[2]]:
                colors[j.split(" ")[2]] = int(j.split(" ")[1])
    s += colors["red"]*colors["green"]*colors["blue"]

print(s)

"""
PART 1
s = 0
id = 0
for ligne in contenu:
    condition = True
    id += 1
    if id >= 10:
        step = len(str(id//10))
    else:
        step = 0
    for i in ligne.strip()[7 + step : len(ligne)].split(";"):
        colors = {"red": 0, "green": 0, "blue": 0}
        for j in i.split(","):
            colors[j.split(" ")[2]] = int(j.split(" ")[1])
        if colors["red"] > 12 or colors["green"] > 13 or colors["blue"] > 14:
            condition = False
    if condition:
        s += id

print(s)
"""
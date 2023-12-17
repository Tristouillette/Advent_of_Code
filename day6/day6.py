#races = [[71530, 940200]]
races = [[41667266, 244104712281040]]

res = []
for race in races:
    possibilities = 0
    for i in range(0, race[0]):
        d = i * (race[0]-i)
        if d > race[1]:
            possibilities += 1
    res.append(possibilities)

print(res)

m = 1
for i in res:
    m *= i

print(m)
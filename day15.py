file = open("input15test.txt", "r")
lines = file.read().split(",")


def HASH(s):
    res = 0
    for i in s:
        res += ord(i)
        res *= 17
        res %= 256
    return res

s = 0
for i in lines:
    print(HASH(i))
    s += HASH(i)

import re
import sys

qds = [0, 0, 0, 0]

rgx = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")

cols = 101
rows = 103
time = 100
robots = []
for line in open("15.in"):
    line = line.strip()
    m = rgx.match(line)
    assert m
    c,r,dc,dr = int(m[1]), int(m[2]), int(m[3]), int(m[4])
    robots.append((r,c, dr, dc))

cache = set()
def draw(t: int):
    pos = set()
    key = []
    for r,c, dr, dc in robots:
        r = (r+dr*t) % rows
        c = (c +dc*t) % cols
        key.append((r,c,dr,dc))
        pos.add((r,c))
    key = tuple(key)
    if key in cache:
        print("CACHE")
        sys.exit()
    cache.add(key)

    for r in range(rows):
        for c in range(cols):
            if (r,c) in pos:
                print("⬜", end="")
            else:
                print("⬛", end="")
        print("")

t = 0
while True:
    print(t, "--------------------------------")
    draw(t)
    t += 1
    #input()






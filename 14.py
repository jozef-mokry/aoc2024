import re
import sys

qds = [0, 0, 0, 0]

rgx = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")

cols = 101
rows = 103
time = 100
for line in sys.stdin:
    line = line.strip()
    m = rgx.match(line)
    assert m
    c,r,dc,dr = int(m[1]), int(m[2]), int(m[3]), int(m[4])

    c = (c + dc * 100)%cols
    r = (r + dr * 100)%rows

    if c < cols // 2:
        if r < rows // 2:
            qds[0] += 1
        elif r > rows // 2:
            qds[1] += 1
    elif c > cols // 2:
        if r < rows // 2:
            qds[2] += 1
        elif r > rows // 2:
            qds[3] += 1

prod = 1
for q in qds:
    prod *= q
print(prod)







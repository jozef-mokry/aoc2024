from collections import defaultdict
import sys


n_cols = 0
antennas = defaultdict(list)
n_rows = 0
grid = []
for r, line in enumerate(sys.stdin):
    n_rows += 1
    line = line.strip()
    grid.append(line)
    n_cols = len(line)
    for c in range(n_cols):
        if line[c] != ".":
            antennas[line[c]].append((r,c))


antinodes = set()

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

for positions in antennas.values():
    for posA in positions:
        for posB in positions:
            if posA == posB:
                continue
            xDiff, yDiff = posB[0] - posA[0], posB[1] - posA[1]
            g = abs(gcd(xDiff, yDiff))
            assert g == 1
            print(xDiff, yDiff, posA, posB, "g", g)
            xDiff //= g
            yDiff //= g
            x, y = posA
            while x >= 0 and y >= 0 and x < n_rows and y < n_cols:
                antinodes.add((x,y))
                x += xDiff
                y += yDiff

for r in range(n_rows):
    for c in range(n_cols):
        if grid[r][c] != ".":
            print(grid[r][c], end="")
        elif (r,c) in antinodes:
            print("#", end="")
        else:
            print(".", end="")
    print("")
print(len(antinodes))


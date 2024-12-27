from collections import defaultdict
import sys


n_cols = 0
antennas = defaultdict(list)
n_rows = 0
for r, line in enumerate(sys.stdin):
    n_rows += 1
    line.strip()
    n_cols = len(line)
    for c in range(n_cols):
        if line[c] != ".":
            antennas[line[c]].append((r,c))


antinodes = set()

for positions in antennas.values():
    for posA in positions:
        for posB in positions:
            if posA == posB:
                continue
            x,y = (2*posB[0] - posA[0], 2*posB[1] - posA[1])
            if x < 0 or y < 0 or x >= n_rows or y >= n_cols:
                continue

            antinodes.add((x,y))
print(len(antinodes))


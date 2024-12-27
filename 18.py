from collections import deque
import sys
bad_pos = set()

N_BYTES = 1024
COLS = 70
ROWS = 70

for i, line in enumerate(sys.stdin):
    if i == N_BYTES:
        break
    line = line.strip()
    col, row = line.split(",")
    bad_pos.add((int(row), int(col)))

q = deque()
q.append((0,0,0))
visited = set()
while q:
    (r, c, steps) = q.popleft()
    if (r,c) in bad_pos:
        continue
    if r < 0 or c < 0 or r > ROWS or c > COLS:
        continue
    if (r,c) in visited:
        continue
    visited.add((r,c))
    if (r,c) == (ROWS,COLS):
        print("SOL", steps)
        break
    for (dr,dc) in [(0,1), (0,-1), (1,0), (-1,0)]:
        q.append((r+dr, c+dc, steps+1))





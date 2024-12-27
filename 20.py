from collections import deque
import sys

grid = [line.strip() for line in sys.stdin]
ROWS = len(grid)
COLS = len(grid[0])
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == 'S':
            S = (r, c)
        if grid[r][c] == 'E':
            E = (r, c)

print("start", S)

def time_to_everywhere(S: tuple[int, int]):
    time_to_everywhere = {}
    q = deque()
    q.append((S, 0))

    while q:
        (r,c), steps = q.popleft()
        if r < 0 or c < 0 or r >= ROWS or c >= COLS:
            continue

        if (r,c) in time_to_everywhere:
            continue

        time_to_everywhere[(r,c)]=steps


        if grid[r][c] == '#':
            continue

        for (dr,dc) in [(0,1), (0,-1), (1,0),(-1,0)]:
            q.append(((r+dr, c+dc), steps+1))
    return time_to_everywhere

from_start = time_to_everywhere(S)
no_cheat_time = from_start[E]
print("no cheat time", no_cheat_time)
from_end = time_to_everywhere(E)

ans = 0
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == '#' and (r,c) in from_start and (r,c) in from_end and from_start[(r,c)] + from_end[(r,c)] <= no_cheat_time - 100:
            ans += 1
print(ans)



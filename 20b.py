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
        if grid[r][c] == '#':
            continue
        for er in range(r-21, r+21):
            for ec in range(c-21, c+21):
                if er < 0 or ec < 0 or er >=ROWS or ec >= COLS:
                    continue
                cheat_time = abs(er-r) + abs(ec-c)
                if cheat_time > 20:
                    continue
                if grid[er][ec] == "#":
                    continue

                if (r,c) not in from_start or (er,ec) not in from_end:
                    continue

                total_time = from_start[(r,c)] + cheat_time + from_end[(er,ec)]
                time_saved = no_cheat_time - total_time
                if time_saved >= 100:
                    ans += 1
print("ans", ans)

# too low: 1004458
# too high?: 1022640

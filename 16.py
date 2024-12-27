from collections import deque
import sys

grid = [[c for c in line.strip()] for line in sys.stdin]
rows = len(grid)
cols = len(grid[0])

s = (0, 0)
e = (0, 0)
best_cost = None
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            s = (r,c)
        if grid[r][c] == "E":
            e = (r,c)

print(s, e)


s_dir = (0, 1)
queue: deque[tuple[tuple[int,int], tuple[int,int], int]]  = deque()
queue.append((s, s_dir, 0))

seen = dict()
while queue:
    ((r,c), (dr, dc), cost) = queue.popleft()
    key = (r,c,dr,dc)
    if key in seen and seen[key] <= cost:
        continue
    if grid[r][c] == "#":
        continue

    seen[key] = cost
    if (r,c) == e:
        if best_cost is None or best_cost > cost:
            best_cost = cost
        continue
    print(key, cost)

    queue.append(((r+dr, c+dc), (dr,dc), cost+1))
    queue.append(((r,c), (-dc, dr), cost+1000))
    queue.append(((r,c), (dc, -dr), cost+1000))
print(best_cost)



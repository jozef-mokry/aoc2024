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
queue: deque[tuple[tuple[int,int], tuple[int,int], int, tuple[int,int,int,int]]]  = deque()
queue.append((s, s_dir, 0, (s[0], s[1], s_dir[0], s_dir[1])))

seen = dict()
prev: dict[tuple[int,int,int,int], set[tuple[int,int,int,int]]] = dict()
while queue:
    ((r,c), (dr, dc), cost, prev_pos) = queue.popleft()
    key = (r,c,dr,dc)
    if key in seen and seen[key] < cost:
        continue
    if grid[r][c] == "#":
        continue

    if key in seen and seen[key] == cost:
        prev[key].add(prev_pos)
    else:
        prev[key] = set([prev_pos])

    seen[key] = cost
    if (r,c) == e:
        if best_cost is None or best_cost > cost:
            best_cost = cost
        continue

    queue.append(((r+dr, c+dc), (dr,dc), cost+1, (r,c,dr,dc)))
    queue.append(((r,c), (-dc, dr), cost+1000, prev_pos))
    queue.append(((r,c), (dc, -dr), cost+1000, prev_pos))
print(best_cost)

visited = set()

def dfs(r, c, dr, dc):
    if (r,c, dr, dc) in visited:
        return
    visited.add((r,c,dr,dc))

    for (pr,pc,pdr, pdc) in prev[(r,c, dr, dc)]:
        dfs(pr, pc, pdr, pdc)

for dr, dc in [(0,1), (0,-1), (1,0),(-1,0)]:
    if seen.get((e[0], e[1], dr, dc)) == best_cost:
        dfs(e[0],e[1],dr,dc)

uniq_pos = set()
for (r,c, _, _) in visited:
    uniq_pos.add((r,c))
print(len(uniq_pos))




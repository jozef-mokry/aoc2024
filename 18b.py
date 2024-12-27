from collections import deque
import sys
bad_pos = set()

COLS = 70
ROWS = 70

bad_pos = []

for i, line in enumerate(sys.stdin):
    line = line.strip()
    col, row = line.split(",")
    bad_pos.append((int(row), int(col)))

def has_path(bad_pos_list: list[int]):
    invalid = set(bad_pos_list)
    q = deque()
    q.append((0,0,0))
    visited = set()
    while q:
        (r, c, steps) = q.popleft()
        if (r,c) in invalid:
            continue
        if r < 0 or c < 0 or r > ROWS or c > COLS:
            continue
        if (r,c) in visited:
            continue
        visited.add((r,c))
        if (r,c) == (ROWS,COLS):
            return True
        for (dr,dc) in [(0,1), (0,-1), (1,0), (-1,0)]:
            q.append((r+dr, c+dc, steps+1))
    return False

print(has_path(bad_pos))
left = 0
right = len(bad_pos)
while left != right:
    mid = (left + right) // 2
    if has_path(bad_pos[:mid]):
        left = mid + 1
    else:
        right = mid
r, c = bad_pos[left-1]
print(f"{c},{r}")





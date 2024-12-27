import sys

def get_key_or_lock() -> None | tuple[list[int], bool]:
    grid = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            break
        grid.append(line)
    if not grid:
        return None
    heights = []
    for c in range(len(grid[0])):
        heights.append(-1)
        for r in range(len(grid)):
            if grid[r][c] == "#":
                heights[-1] += 1
    is_lock = grid[0] == "#" * 5
    return heights, is_lock

keys = []
locks = []
while True:
    v = get_key_or_lock()
    if v is None:
        break
    h, is_lock = v
    if is_lock:
        locks.append(h)
    else:
        keys.append(h)
ans = 0
for k in keys:
    for l in locks:
        for (h, hh) in zip(k,l):
            if h+hh >= 6:
                break
        else:
            ans += 1
print(ans)

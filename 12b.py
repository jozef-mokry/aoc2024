import sys
grid = [[c for c in line.strip()] for line in sys.stdin]

visited = set()

def dfs(r, c, letter, dr, dc, vertical: list[list[tuple[int, bool]]], horizontal: list[list[tuple[int, bool]]]):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != letter:
        match (dr, dc):
            case (0, 1):
                vertical[c].append((r, True))
            case (0, -1):
                vertical[c+1].append((r, False))
            case (1, 0):
                horizontal[r].append((c, True))
            case (-1, 0):
                horizontal[r+1].append((c, False))

        return 0, 1



    if (r,c) in visited:
        return 0, 0
    visited.add((r,c))


    area = 1
    perimeter = 0

    for (dr, dc) in [(0,1), (0,-1), (1,0), (-1, 0)]:
        a, p = dfs(r+dr, c+dc, letter, dr, dc, vertical, horizontal)
        area += a
        perimeter += p
    return area, perimeter

def count_segments(edges: list[list[tuple[int, bool]]]):
    segments = 0
    for row in edges:
        row.sort()
        prev = None
        prev_side = None
        for v, side in row:
            if v - 1 != prev or side != prev_side:
                segments += 1
            prev = v
            prev_side = side
    return segments

ans = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        horizontal = [[] for _ in range(len(grid)+1)]
        vertical = [[] for _ in range(len(grid[0]) + 1)]
        area, _ = dfs(r,c, grid[r][c], 0, 0, horizontal, vertical)
        perimeter = count_segments(horizontal) + count_segments(vertical)
        print(grid[r][c], area, perimeter)
        ans += area * perimeter
print(ans)


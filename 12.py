import sys
grid = [[c for c in line.strip()] for line in sys.stdin]

visited = set()

def dfs(r, c, letter):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != letter:
        return 0, 1

    if (r,c) in visited:
        return 0, 0
    visited.add((r,c))


    area = 1
    perimeter = 0

    for (dr, dc) in [(0,1), (0,-1), (1,0), (-1, 0)]:
        a, p = dfs(r+dr, c+dc, letter)
        area += a
        perimeter += p
    return area, perimeter

ans = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        area, perimeter = dfs(r,c, grid[r][c])
        print(grid[r][c], area, perimeter)
        ans += area * perimeter
print(ans)


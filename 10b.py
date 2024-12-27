import sys

grid = [[int(v) for v in line.strip()] for line in sys.stdin]

def dfs(grid, r, c, visited, expected):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or (r,c) in visited:
        return 0
    if grid[r][c] != expected:
        return False
    #visited.add((r,c))
    if grid[r][c] == 9:
        return 1
    ans = 0
    for dx, dy in [(0,1), (0, -1), (1,0), (-1, 0)]:
        ans += dfs(grid, r+dx, c+dy, visited, expected+1)
    return ans

ans = 0

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 0:
            ans += dfs(grid, r, c, set(), 0)
print(ans)

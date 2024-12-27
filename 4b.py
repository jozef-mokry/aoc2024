import re
import sys

grid = [line.strip() for line in sys.stdin]

MS = set(["M", "S"])
def check(r, c):
    if grid[r][c] != "A":
        return False
    def get(r, c):
        if r < 0 or r >= len(grid):
            return None
        if c < 0 or c >= len(grid[0]):
            return None
        return grid[r][c]


    return set([ get(r-1, c-1), get(r+1, c+1)]) == MS and set([ get(r-1, c+1), get(r+1, c-1)]) == MS


ans = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if check(r,c):
            ans += 1
print(ans)


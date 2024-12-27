import re
import sys

grid = [line.strip() for line in sys.stdin]
r_xmas = r"XMAS"
r_samx = r"SAMX"

def collect(start, move):
    line = ""
    while start[0] >= 0 and start[0] < len(grid) and start[1] >= 0 and start[1] < len(grid[0]):
        line += grid[start[0]][start[1]]
        start[0] += move[0]
        start[1] += move[1]
    return line

ans = 0
# horizontal
for line in grid:
    ans += len(re.findall(r_xmas, line))
    ans += len(re.findall(r_samx, line))

print(ans)

# vertical
for col in range(len(grid[0])):
    line = collect(start=[0, col], move=[1, 0])
    ans += len(re.findall(r_xmas, line))
    ans += len(re.findall(r_samx, line))

print(ans)

# diagonals starting at the beginning or end of row
for r in range(len(grid)):
    line = collect(start=[r, 0], move=[1, 1])
    ans += len(re.findall(r_xmas, line))
    ans += len(re.findall(r_samx, line))

    line = collect(start=[r, len(grid[0]) - 1], move=[1, -1])
    ans += len(re.findall(r_xmas, line))
    ans += len(re.findall(r_samx, line))

# diagonals starting from the first row
for c in range(1, len(grid[0])):
    line = collect(start=[0, c], move=[1, 1])
    ans += len(re.findall(r_xmas, line))
    ans += len(re.findall(r_samx, line))

    line = collect(start=[0, c - 1], move=[1, -1])
    ans += len(re.findall(r_xmas, line))
    ans += len(re.findall(r_samx, line))

print(ans)


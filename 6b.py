import sys

grid = [[c for c in line.strip()] for line in sys.stdin]

posR: int = 0
posC: int = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "^":
            posR, posC = r,c
            break

dirR, dirC = -1, 0
ans = 0
visited = []
def next_pos():
    global ans, dirR, dirC, posR, posC
    if grid[posR][posC] != 'X':
        grid[posR][posC] = 'X'
        visited.append((posR, posC))
        ans += 1
    while True:
        nextR, nextC = posR+dirR, posC+dirC
        if nextR < 0 or nextC < 0 or nextR >= len(grid) or nextC >= len(grid[0]):
            return None, None
        if grid[nextR][nextC] != '#':
            return nextR, nextC


        # rotate by 90 degrees right
        dirR, dirC = dirC, -dirR


while True:
    newR, newC = next_pos()
    if newR == None or newC == None:
        break
    posR, posC = newR, newC
print(ans)

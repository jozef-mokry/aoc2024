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
startR, startC = posR, posC
visited = set()
visited_dir = set()
def next_pos(save_visited=True):
    global dirR, dirC, posR, posC
    global visited_dir
    if save_visited:
        visited.add((posR, posC))
    if (posR, posC, dirR, dirC) in visited_dir:
        return -1, -1
    visited_dir.add((posR, posC, dirR, dirC))
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

print("visited", len(visited))
ans = 0

def loops(r, c):
    global dirR, dirC
    global posR, posC
    global visited_dir
    global grid
    visited_dir = set()
    v = grid[r][c]
    grid[r][c] = '#'

    posR, posC = startR, startC
    dirR, dirC = -1, 0
    while True:
        newR, newC = next_pos(save_visited=False)
        if newR == None or newC == None:
            loops = False
            break
        if newR == -1:
            loops = True
            break
        posR, posC = newR, newC

    grid[r][c] = v
    return loops

for (r, c) in visited:
    if (r,c) == (startR, startC):
        continue
    if loops(r,c):
        ans += 1

print(ans)

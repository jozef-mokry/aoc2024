import sys

grid = []
for line in sys.stdin:
    line = line.strip()
    if line == "":
        break
    grid.append([c for c in line])

dirs = []
for line in sys.stdin:
    line = line.strip()
    dirs.extend([c for c in line])

rows = len(grid)
cols = len(grid[0])
pos_r, pos_c = 0, 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "@":
            pos_r, pos_c = r,c
            break

print(pos_r, pos_c)

dir_map = {
        "^": (-1, 0),
        "v": (1, 0),
        ">": (0, 1),
        "<": (0, -1),
}

def move(r, c, d):
    if grid[r][c] == "#":
        return False
    if grid[r][c] == ".":
        return True
    dr, dc = d
    if move(r+dr, c+dc, d):
        grid[r+dr][c+dc] = grid[r][c]
        grid[r][c] = "."
        return True
    return False

def draw():
    for r in range(rows):
        for c in range(cols):
            print(grid[r][c], end="")
        print("")
    print("")

for d in dirs:
    draw()
    print(d*10)
    dr, dc = dir_map[d]
    if move(pos_r, pos_c, dir_map[d]):
        pos_r += dr
        pos_c += dc
draw()

ans = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "O":
            ans += 100*r + c
print(ans)



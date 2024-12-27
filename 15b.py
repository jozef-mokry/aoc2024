import sys

grid = []
for line in sys.stdin:
    line = line.strip()
    if line == "":
        break
    grid.append([c for c in line])

new_grid = []
for row in grid:
    new_row = []
    for c in row:
        match c:
            case "#":
                new_row.extend(["#", "#"])
            case ".":
                new_row.extend([".", "."])
            case "O":
                new_row.extend(["[", "]"])
            case "@":
                new_row.extend(["@", "."])
            case _:
                assert False, c
    new_grid.append(new_row)

grid = new_grid

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

def can_move(r,c,d,cache):
    if (r,c) in cache:
        return cache[(r,c)]

    cache[(r,c)] = True

    if grid[r][c] == "#":
        return False
    if grid[r][c] == ".":
        return True

    dr, dc = d
    if grid[r][c] == "@":
        ans = can_move(r+dr, c+dc, d, cache)
    elif grid[r][c] == "[":
        ans = can_move(r+dr, c+dc, d, cache) and can_move(r, c+1, d, cache)
    else:
        assert grid[r][c] == "]", grid[r][c]
        ans = can_move(r+dr, c+dc, d, cache) and can_move(r, c-1, d, cache)
    cache[(r,c)] = ans
    return ans

def move(r, c, d, cache):
    if grid[r][c] == "#":
        assert False
    if grid[r][c] == ".":
        return
    if (r,c) in cache:
        return
    cache.add((r,c))
    dr, dc = d
    if grid[r][c] == "@":
        move(r+dr, c+dc, d, cache)
        grid[r+dr][c+dc] = '@'
        grid[r][c] = '.'
    elif grid[r][c] == "[":
        move(r+dr, c+dc, d, cache)
        move(r, c+1, d, cache)
        grid[r+dr][c+dc] = '['
        grid[r][c] = '.'
    else:
        assert grid[r][c] =="]", grid[r][c]
        move(r+dr, c+dc, d, cache)
        move(r, c-1, d, cache)
        grid[r+dr][c+dc] = ']'
        grid[r][c] = '.'

def draw():
    for r in range(rows):
        for c in range(cols):
            print(grid[r][c], end="")
        print("")
    print("")

for d in dirs:
    #draw()
    print(d*10)
    dr, dc = dir_map[d]
    if can_move(pos_r, pos_c, dir_map[d], {}):
        move(pos_r,pos_c,dir_map[d], set())
        pos_r += dr
        pos_c += dc
draw()

ans = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "[":
            ans += 100*r + c
print(ans)

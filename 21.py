from collections import deque
from functools import cache
import sys
ans = 0

NUM_DIR_PADS = 25 # change this for part1 to 2

def shortest_sequence(code: str) -> int:
    curr_key = 'A'
    steps = 0
    for target_key in code:
        steps += numeric_press_key(curr_key, target_key)
        curr_key = target_key
    return steps

num_pad = [
        ["7","8","9"],
        ["4","5","6"],
        ["1","2","3"],
        ["X","0","A"],
]
num_to_pos = {}
for r in range(len(num_pad)):
    for c in range(len(num_pad[0])):
        num_to_pos[num_pad[r][c]] = (r,c)

dir_pad = [
        ["X", "^", "A"],
        ["<", "v", ">"],
]
dir_to_pos = {}
for r in range(len(dir_pad)):
    for c in range(len(dir_pad[0])):
        dir_to_pos[dir_pad[r][c]] = (r,c)

def all_paths(start: tuple[int,int], end: tuple[int,int], pad: list[list[str]]) -> list[list[tuple[int,int]]]:
    # find all paths between start and end
    paths: list[list[tuple[int,int]]] = []
    q: deque[tuple[tuple[int,int], list[tuple[int,int]]]] = deque()
    q.append((start, []))
    while q:
        (r,c), path = q.popleft()
        if r < 0 or c < 0 or r >= len(pad) or c >= len(pad[0]) or pad[r][c] == 'X':
            continue
        if (r,c) in path:
            continue
        path = [*path, (r,c)]
        if (r,c) == end:
            paths.append(path)
        else:
            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                q.append(((r+dr,c+dc), path))
    return paths

@cache
def numeric_press_key(curr_key: str, target_key: str) -> int:
    start = num_to_pos[curr_key]
    end = num_to_pos[target_key]
    best = None
    paths = all_paths(start, end, num_pad)
    for path in paths:
        steps = 0
        curr_dir_key = "A"
        for target_dir_key in convert_to_buttons(path):
            steps += directional_press_key(curr_dir_key, target_dir_key, NUM_DIR_PADS)
            curr_dir_key = target_dir_key
        steps += directional_press_key(curr_dir_key, "A", NUM_DIR_PADS)
        if best is None or steps < best:
            best = steps
    assert best is not None
    return best

@cache
def directional_press_key(curr_key: str, target_key: str, level: int) -> int:
    if level == 0:
        # this is the pad in my hands, press the button directly
        return 1
    start = dir_to_pos[curr_key]
    end = dir_to_pos[target_key]
    best = None
    paths = all_paths(start, end, dir_pad)
    for path in paths:
        steps = 0
        curr_dir_key = "A"
        for target_dir_key in convert_to_buttons(path):
            steps += directional_press_key(curr_dir_key, target_dir_key, level-1)
            curr_dir_key = target_dir_key
        steps += directional_press_key(curr_dir_key, "A", level-1)
        if best is None or steps < best:
            best = steps
    assert best is not None
    return best

def convert_to_buttons(path: list[tuple[int,int]]):
    buttons = ""
    for (r,c), (rr,cc) in zip(path, path[1:]):
        match (rr-r, cc-c):
            case (0,1):
                buttons += ">"
            case (0,-1):
                buttons += "<"
            case (1,0):
                buttons += "v"
            case (-1,0):
                buttons += "^"
            case x:
                assert False, x
    return buttons

for line in sys.stdin:
    line = line.strip()
    steps = shortest_sequence(line)
    ans += steps * int(line[:-1])
print(ans)

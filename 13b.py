import re
import sys

def solve(ax:int, ay: int, bx: int, by: int, x: int, y: int):
    """
    Solve:
    a * ax + b * bx = x
    a * ay + b * by = y
    """
    det = ax*by - ay*bx
    if det == 0:
        # (ax, ay) and (bx, by) are parallel
        # is there k s.t.:
        # ax * k = x and ay * k = y
        if ay * x != ax * y:
            return None

        # there are infinite solutions
        # B is cheaper so start with that
        b = x // bx
        while True:
            a = (x - b*bx) // ax
            if a * ax + b*bx == x and a*ay + b*by == y:
                return 3*a + b
            b -= 1


    a = (x*by - y*bx) / det
    b = (ax * y - ay * x) / det
    if a == int(a) and b == int(b):
        return 3*a + b
    else:
        return None

ans = 0
button_re = re.compile(r"Button (A|B): X\+(\d+), Y\+(\d+)")
prize_re = re.compile(r"Prize: X=(\d+), Y=(\d+)")
for i, line in enumerate(sys.stdin):
    line = line.strip()
    match i % 4:
        case 0:
            m = button_re.match(line)
            assert m
            ax, ay = int(m[2]), int(m[3])
        case 1:
            m = button_re.match(line)
            assert m
            bx, by = int(m[2]), int(m[3])
        case 2:
            m = prize_re.match(line)
            assert m

            x, y = int(m[1]), int(m[2])
            x += 10000000000000
            y += 10000000000000
            cost = solve(ax, ay, bx, by, x, y)
            if cost is not None:
                ans += cost

        case 3:
            assert line == ""
print(ans)

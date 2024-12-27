import re
import sys

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
            best_cost = None
            pos_x, pos_y = 0, 0
            x, y = int(m[1]), int(m[2])
            for a in range(101):
                for b in range(101):
                    if a*ax + b*bx != x or a*ay + b*by != y:
                        continue
                    cost = a*3 + b*1
                    if best_cost is None or best_cost > cost:
                        best_cost = cost
            if best_cost is not None:
                ans += best_cost
        case 3:
            assert line == ""
print(ans)

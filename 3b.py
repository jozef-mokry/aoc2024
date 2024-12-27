import re
import sys

ans = 0
active = True
for line in sys.stdin:
    for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)", line):
        if match.group(0).startswith("mul"):
            if active:
                a,b = match.group(1), match.group(2)
                ans += int(a)*int(b)
        elif match.group(0).startswith("don't"):
            active = False
        else:
            active = True
print(ans)

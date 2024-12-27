import re
import sys

ans = 0
for line in sys.stdin:
    for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", line):
        a,b = match.group(1), match.group(2)
        ans += int(a)*int(b)
print(ans)

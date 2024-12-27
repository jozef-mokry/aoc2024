import sys
a, b = [], []
for line in sys.stdin:
    x,y = [int(x) for x in line.split()]
    a.append(x)
    b.append(y)
counts = {}
for x in b:
    counts.setdefault(x, 0)
    counts[x] += 1
ans = 0
for x in a:
    ans += x*counts.get(x, 0)
print(ans)

import sys
a, b = [], []
for line in sys.stdin:
    x,y = [int(x) for x in line.split()]
    a.append(x)
    b.append(y)
a.sort()
b.sort()
ans = 0
for x,y in zip(a,b):
    ans += abs(x-y)
print(ans)

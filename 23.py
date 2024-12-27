from collections import defaultdict
import sys

edges = defaultdict(set)
for line in sys.stdin:
    a, b = line.strip().split("-")
    edges[a].add(b)
    edges[b].add(a)

triangles = set()
for v, ns in edges.items():
    for n in ns:
        shared = edges[v] & edges[n]
        for s in shared:
            triangle = tuple(sorted([v,n,s]))
            triangles.add(triangle)

ans = 0
for (a,b,c) in triangles:
    if a.startswith("t") or b.startswith("t") or c.startswith("t"):
        ans += 1
print(ans)

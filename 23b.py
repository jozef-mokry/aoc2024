from collections import defaultdict
import sys

edges = defaultdict(set)
for line in sys.stdin:
    a, b = line.strip().split("-")
    edges[a].add(b)
    edges[b].add(a)

cliques = set([(v,) for v in edges])

def extend(cliques: set[tuple]) -> set[tuple]:
    new_cliques = set()

    for (v, *vs) in cliques:
        e = edges[v]
        for vv in vs:
            e = e & edges[vv]
        for new_v in e:
            new_cliques.add(tuple(sorted([v, *vs, new_v])))
    return new_cliques

i = 1
while len(cliques) > 1:
    print(i, len(cliques))
    cliques = extend(cliques)
    i += 1

sol = next(iter(cliques))
print(",".join(sol))



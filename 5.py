from collections import defaultdict
import sys
rules = defaultdict(set)
for line in sys.stdin:
    line = line.strip()
    if line == "":
        break
    precondition, val = [int(v) for v in line.split("|")]

    rules[val].add(precondition)

print(rules)
ans = 0
def is_valid(vals: list[int]) -> bool:
    seen = set()
    vals_set = set(vals)
    for v in vals:
        for precondition in rules[v]:
            if precondition not in vals_set:
                continue
            if precondition not in seen:
                print("requires", precondition, "before", v)
                return False
        seen.add(v)
    return True

for line in sys.stdin:
    vals = [int(v) for v in line.strip().split(",")]
    print(vals)
    if is_valid(vals):
        ans += vals[len(vals)//2]

print(ans)

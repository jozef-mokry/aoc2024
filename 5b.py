from collections import defaultdict
import sys
rules = defaultdict(set)
for line in sys.stdin:
    line = line.strip()
    if line == "":
        break
    precondition, val = [int(v) for v in line.split("|")]

    rules[val].add(precondition)

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

def dfs(v: int, seen: set[int], fixed: list[int], vals_set: set[int]):
    if v in seen:
        return
    seen.add(v)

    for prec in rules[v]:
        if prec in vals_set:
            dfs(prec, seen, fixed, vals_set)
    fixed.append(v)

def fix(vals: list[int]) -> list[int]:

    fixed = []
    vals_set = set(vals)

    seen = set()
    for v in vals:
        dfs(v, seen, fixed, vals_set)
    return fixed


for line in sys.stdin:
    vals = [int(v) for v in line.strip().split(",")]
    if not is_valid(vals):
        correct = fix(vals)
        ans += correct[len(correct)//2]

print(ans)

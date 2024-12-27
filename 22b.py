from collections import defaultdict
import sys

seeds = [int(line) for line in sys.stdin]

MOD = 16777216
def get_next(val: int) -> int:
    val = ((val * 64) ^ val ) % MOD
    val = ((val // 32) ^ val) % MOD
    return ((val * 2048) ^ val) % MOD

best_for_diff = defaultdict(int)
for seed in seeds:
    seen_diff = set()
    a = seed
    b = get_next(a)
    c = get_next(b)
    d = get_next(c)
    for _ in range(2000 - 3):
        new = get_next(d)
        diff = (b%10-a%10, c%10-b%10, d%10-c%10, new%10-d%10)
        if diff not in seen_diff:
            best_for_diff[diff] += new%10
            seen_diff.add(diff)
        a,b,c,d = b,c,d,new
print(max(best_for_diff.values()))

import sys
seeds = [int(line) for line in sys.stdin]

MOD = 16777216
def get_next(val: int) -> int:
    val = ((val * 64) ^ val ) % MOD
    val = ((val // 32) ^ val) % MOD
    return ((val * 2048) ^ val) % MOD

ans = 0
for seed in seeds:
    for _ in range(2000):
        seed = get_next(seed)
    ans += seed
print(ans)



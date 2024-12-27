import sys
towels = sys.stdin.readline().strip().split(", ")

patterns = sys.stdin.read().split()

mem = {}
def possible(p):
    if p in mem:
        return mem[p]
    if p == "":
        return 1

    ans = 0
    for t in towels:
        if p.startswith(t):
            ans += possible(p[len(t):])

    mem[p] = ans
    return ans

ans = 0
for p in patterns:
    ans += possible(p)

print(ans)

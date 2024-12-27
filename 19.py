import sys
towels = sys.stdin.readline().strip().split(", ")

patterns = sys.stdin.read().split()

mem = {}
def possible(p):
    if p in mem:
        return mem[p]
    if p == "":
        return True
    for t in towels:
        if p.startswith(t):
            if possible(p[len(t):]):
                mem[p] = True
                return True

    mem[p] = False
    return False

ans = 0
for p in patterns:
    if possible(p):
        print(p)
        ans += 1

print(ans)

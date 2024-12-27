import sys

mem: dict[str, int] = {}
for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    name, val = line.split(": ")
    mem[name] = int(val)

rules: dict[str, tuple[str, str, str]] = {} # out <- a b op
for line in sys.stdin:
    line = line.strip()
    a, op, b, _, out = line.split(" ")
    rules[out] = (a, b, op)

def compute(reg: str) -> int:
    if reg in mem:
        return mem[reg]
    match rules[reg]:
        case (a, b, "XOR"):
            ans = compute(a) ^ compute(b)
        case (a, b, "AND"):
            ans = compute(a) & compute(b)
        case (a, b, "OR"):
            ans = compute(a) | compute(b)
        case _:
            assert False, rules[reg]
    mem[reg] = ans
    assert ans in (0,1)
    return ans

zs = 0
for v in rules:
    if v.startswith("z"):
        zs += 1
        compute(v)

ans = 0
for idx in reversed(range(zs)):
    ans = ans*2 + compute(f"z{idx:02}")
print(ans)

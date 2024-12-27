import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        break

rules: dict[str, tuple[str, str, str]] = {} # out <- a b op
for line in sys.stdin:
    line = line.strip()
    a, op, b, _, out = line.split(" ")
    rules[out] = (a, b, op)

def compute(reg: str, mem: dict[str, int]) -> int:
    if reg in mem:
        return mem[reg]
    match rules[reg]:
        case (a, b, "XOR"):
            ans = compute(a, mem) ^ compute(b, mem)
        case (a, b, "AND"):
            ans = compute(a, mem) & compute(b, mem)
        case (a, b, "OR"):
            ans = compute(a, mem) | compute(b, mem)
        case _:
            assert False, rules[reg]
    mem[reg] = ans
    assert ans in (0,1)
    return ans

BITS = 45
def check(bit_idx: int):
    mem = {}
    print(f"---------{bit_idx}---------")
    for i in range(BITS):
        mem[f"x{i:02}"] = 1 if i == bit_idx else 0
        mem[f"y{i:02}"] = 0
    for i in range(BITS+1):
        v = compute(f"z{i:02}", mem)
        if i == bit_idx:
            if v != 1:
                print("Expected 1, but got", v, "at pos", i)
        else:
            if v != 0:
                print("Expected 0, but got", v, "at pos", i)
for i in range(BITS):
    check(i)
# manually inspect input rules for the bits that did not pass check
bad = ["vcf", "z10", "fhg", "z17", "fsq", "dvb", "z39", "tnc"]
print(",".join(sorted(bad)))

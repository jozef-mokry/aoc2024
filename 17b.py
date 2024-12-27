#Register A: 25358015
#Register B: 0
#Register C: 0
#
#Program: 2,4,1,1,7,5,0,3,4,7,1,6,5,5,3,0

regs = [25358015, 0, 0]
prog = [2,4,1,1,7,5,0,3,4,7,1,6,5,5,3,0]

def literal(pc: int) -> int:
    return prog[pc]

def combo(pc: int) -> int:
    v = prog[pc]
    if 0 <= v <= 3:
        return v
    if 4 <= v <= 6:
        return regs[v - 4]
    assert False, v

def pretty(instr: int, v: int):
    def combo_pretty():
        if 0 <= v <= 3:
            return v
        if 4 <= v <= 6:
            return ["A", "B", "C"][v - 4]
        assert False, v

    def literal_pretty():
        return v

    match instr:
        case 0:
            print(f"A = A / 2^{combo_pretty()}")
        case 1:
            print(f"B = B xor {literal_pretty()}")
        case 2:
            print(f"B = {combo_pretty()} % 8")
        case 3:
            print(f"if A != 0: goto {literal_pretty()}")
        case 4:
            print(f"B = B xor C")
        case 5:
            print(f"output {combo_pretty()} % 8")
        case 6:
            print(f"B = A / 2^{combo_pretty()}")
        case 7:
            print(f"C = A / 2^{combo_pretty()}")
        case v:
            assert False, f"invalid instr: {instr}"

def run(pc: int, output: list[int]) -> int:
    if pc >= len(prog):
        return -1 # halt

    match prog[pc]:
        case 0:
            # division
            regs[0] = regs[0] // (2**combo(pc+1))
        case 1:
            regs[1] = regs[1] ^ literal(pc+1)
        case 2:
            regs[1] = combo(pc+1) % 8
        case 3:
            if regs[0] != 0:
                return literal(pc+1)
        case 4:
            regs[1] = regs[1] ^ regs[2]
        case 5:
            output.append(combo(pc+1) % 8)
        case 6:
            regs[1] = regs[0] // (2**combo(pc+1))
        case 7:
            regs[2] = regs[0] // (2**combo(pc+1))
        case v:
            assert False, f"invalid pc: {v}"
    return pc + 2

pc = 0
output = []
while pc != -1:
    pc = run(pc, output)
print(",".join([str(v) for v in output]))

for instr, v in zip(prog[::2], prog[1::2]):
    pretty(instr, v)

A = 0
print(prog)

def search(prog: list[int], A: int):
    if not prog:
        return A, True

    goal = prog.pop()
    for last_digit in range(8):
        new_A = A * 8 + last_digit
        B = last_digit ^ 1
        C = new_A // (2**B)
        if (B ^ C ^ 6) % 8 == goal:
            sol, found = search(prog, new_A)
            if found:
                return sol, True
    prog.append(goal)
    return -1, False

print("SOL", search(prog, 0))

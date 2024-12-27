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

import sys

def safe(nums: list[int]) -> bool:
    inc, dec = False, False
    for a, b in zip(nums, nums[1:]):
        if a==b:
            return False
        if abs(a-b) > 3:
            return False
        if a > b:
            inc = True
        else:
            dec = True
        if inc and dec:
            return False
    return True


def safe2(nums: list[int]) -> bool:
    inc, dec = False, False
    for a, b in zip(nums, nums[1:]):
        if a==b:
            return False
        if abs(a-b) > 3:
            return False
        if a > b:
            inc = True
        else:
            dec = True
        if inc and dec:
            return False
    return True

ans = 0
ans2 = 0
for line in sys.stdin:
    line = [int(x) for x in line.split()]
    if safe(line):
        ans += 1
        ans2 += 1
        continue
    if any(safe(line[:i] + line[i+1:]) for i in range(len(line))):
        ans2+= 1
print(ans)
print(ans2)

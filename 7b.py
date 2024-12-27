import sys

ans = 0

def join(a: int, b: int) -> int:
    x = b
    while x > 0:
        x //= 10
        a *= 10
    a += b
    return a

def good(nums: list[int], goal: int, curr: int, pos: int = 0) -> bool:
    if curr > goal:
        return False
    if pos == len(nums):
        return goal == curr
    return good(nums, goal, curr + nums[pos], pos + 1) or good(nums, goal, curr * nums[pos], pos + 1) or good(nums, goal, join(curr, nums[pos]), pos+1)

for line in sys.stdin:
    goal, nums = line.strip().split(": ")
    goal = int(goal)
    nums = [int(v) for v in nums.split(" ")]
    if good(nums, goal, 0):
        ans += goal
print(ans)


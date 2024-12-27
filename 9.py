from collections import deque
import sys
disk = sys.stdin.read().strip()

segments = [int(c) for c in disk]
switch = deque([segments[0]])
for s in segments[1:]:
    switch.append(switch[-1] + s)
print(switch)
blocks = deque(enumerate(segments[0::2]))
for b_id, b in blocks:
    assert b > 0
free = segments[1::2]
total = sum(b[1] for b in blocks)
print(total, len(blocks), len(free))


ans = 0
read_from_start = True
for i in range(total):
    while i == switch[0]:
        read_from_start = not read_from_start
        switch.popleft()

    # remove empty blocks

    assert blocks[0][1] > 0
    assert blocks[-1][1] > 0
    if read_from_start:
        #print(i, '*', blocks[0][0])
        print(blocks[0][0], end="")
        ans += i*blocks[0][0]
        blocks[0] = (blocks[0][0], blocks[0][1] - 1)
        if blocks[0][1] == 0:
            blocks.popleft()
    else:
        #print(i, '*', blocks[-1][0])
        print(blocks[-1][0], end="")
        ans += i*blocks[-1][0]
        blocks[-1] = (blocks[-1][0], blocks[-1][1] - 1)
        if blocks[-1][1] == 0:
            blocks.pop()

print("")
print(ans)







from collections import deque
import sys
disk = sys.stdin.read().strip()

segments = [int(c) for c in disk]
free: list[list[int]] = [[] for _ in range(10)]
ans = 0
blocks: list[tuple[int,int,int]] = []

pos = 0
for i, seg_len in enumerate(segments):
    if i % 2 == 1:
        # free space
        free[seg_len].append(pos)
    else:
        blocks.append((i//2, seg_len, pos))
    pos += seg_len
for f in free:
    f.sort(reverse=True)

ans = 0
print("free", free)
for (id_, block_len, block_pos) in reversed(blocks):
    assert block_len > 0
    # lets see if there's space for this block
    candidates = [i for i in range(block_len, len(free)) if len(free[i]) > 0]
    if len(candidates) > 0:
        candidates.sort(key=lambda i: free[i][-1])
        c = candidates[0]
        assert len(candidates) == 1 or free[candidates[1]][-1] > free[c][-1]

        # we found a place
        new_block_pos = free[c][-1]
        if new_block_pos < block_pos:
            block_pos = new_block_pos
            #print("moving", id_, "to pos:", block_pos)
            free[c].pop()

            remains = c - block_len
            assert remains >= 0
            if remains > 0:
                free[remains].append(block_pos + block_len)
                free[remains].sort(reverse=True)
    for p in range(block_pos, block_pos+block_len):
        print(p, '*',  id_)
        ans += p*id_




print(ans)




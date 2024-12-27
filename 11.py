cache = {}

def dig(stone):
    a = 0
    while stone > 0:
        stone //= 10
        a +=1
    return a

def split(stone):
    d = dig(stone) // 2
    div = 1
    while d > 0:
        d -= 1
        div *= 10
    return stone // div, stone % div

def count(stone, steps):
    if (stone, steps) in cache:
        return cache[(stone,steps)]

    if steps == 0:
        #print(stone)
        return 1

    if stone == 0:
        ans = count(1, steps-1)

    elif dig(stone) % 2 == 0:
        left, right = split(stone)
        ans = count(left, steps-1) + count(right, steps-1)

    else:
        ans = count(stone*2024, steps-1)
    cache[(stone,steps)] = ans
    return ans

stones = [8793800, 1629, 65, 5, 960, 0, 138983, 85629]
#stones = [125, 17]

print(sum(count(stone, 75) for stone in stones))

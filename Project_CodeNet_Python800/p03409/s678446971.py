n = int(input())
red = [list(map(int, input().split())) for _ in range(n)]
blue = [list(map(int, input().split())) for _ in range(n)]

blue.sort()

res = 0
for bx, by in blue:
    dist = -1
    for rx, ry in red:
        if rx < bx and dist < ry < by:
            dist = ry
            mx, my = rx, ry
    
    if dist > -1:
        res += 1
        red.remove([mx, my])

print(res)
n = int(input())

reds = [tuple(map(int, input().split())) for _ in range(n)]
blues = [tuple(map(int, input().split())) for _ in range(n)]

blues.sort(key=lambda x:x[0])
reds.sort(key=lambda x:x[1])

count = 0
for b in blues:
    bx, by = b
    for r in reds[::-1]:
        rx, ry = r
        if bx > rx and by > ry:
            count += 1
            reds.remove(r)
            break

print(count)

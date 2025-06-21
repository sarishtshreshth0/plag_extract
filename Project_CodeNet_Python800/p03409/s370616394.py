N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
CD = [tuple(map(int, input().split())) for _ in range(N)]

AB.sort(key = max, reverse = True)
CD.sort(key = min)

counter = 0
for a, b in AB:
    for c, d in CD:
        if a < c and b < d:
            CD.remove( (c, d) )
            counter += 1
            break

print(counter)

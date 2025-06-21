N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
CD = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(N):
    AB[i] = (AB[i][0] + 1000000, AB[i][1])
    CD[i] = (CD[i][0] + 1000000, CD[i][1])

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

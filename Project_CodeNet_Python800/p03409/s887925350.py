N = int(input())
AB = [tuple(map(int,input().split())) for i in range(N)]
CD = [tuple(map(int,input().split())) for i in range(N)]
AB.sort(key=lambda x: x[0])
CD.sort(key=lambda x: x[0])
ans = 0
for c,d in CD:
    idx = 10000
    for i in range(N):
        if AB[i] == -1:
            continue
        if c < AB[i][0]:
            break
        if AB[i][1] < d:
            if idx == 10000:
                idx = i
            elif AB[idx][1] < AB[i][1]:
                idx = i
    if idx != 10000:
        ans += 1
        AB[idx] = -1
print(ans)
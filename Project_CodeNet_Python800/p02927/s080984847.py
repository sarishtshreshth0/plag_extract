M, D = map(int,input().split())

ans = 0
for i in range(1, M+1):
    for j in range(11, D+1):
        j = str(j)
        k = int(j[0])
        l = int(j[1])
        if k >= 2 and l >= 2 and i == k * l:
            ans += 1

print(ans)
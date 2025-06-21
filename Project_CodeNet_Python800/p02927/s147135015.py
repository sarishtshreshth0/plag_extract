M, D = map(int, input().split())

ans = 0

for i in range(1, M+1):
    for j in range(1, D+1):
        if len(str(j)) >= 2:
            if int(str(j)[0]) >= 2 and int(str(j)[1]) >= 2 and int(str(j)[0]) * int(str(j)[1]) == i:
                ans += 1


print(ans)

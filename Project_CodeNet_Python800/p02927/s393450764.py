M, D = map(int, input().split())
cnt = 0
for m in range(1, M + 1):
    for d in range(22, D + 1):
        d1, d10 = int(str(d)[1]), int(str(d)[0])
        if d1 >= 2 and d1 * d10 == m:
            cnt += 1
print(cnt)
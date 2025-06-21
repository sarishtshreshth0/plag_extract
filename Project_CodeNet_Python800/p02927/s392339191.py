M, D = map(int, input().split())
ans = 0
for m in range(1, M+1):
    for d in range(22, D+1):
        d_10, d_1 = divmod(d, 10)
        if d_10 > 1 and d_1 > 1 and d_10*d_1==m:
            ans += 1
print(ans)
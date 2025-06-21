m, d = list(map(int, input().split()))
ans = 0
for mm in range(1, m+1):
    for dd in range(1, d+1):
        if dd % 10 >= 2 and dd//10 >= 2 and mm == (dd % 10)*(dd//10):
            ans += 1


print(ans)

m, d = map(int, input().split())

ans = 0


for i in range(1,m+1):
    for j in range(1, d+1):
        if len(str(j)) == 1:
            continue
        d1 = j%10
        d2 = j//10
        if d1 >= 2 and d2 >= 2 and d1*d2==i:
            ans += 1

print(ans)
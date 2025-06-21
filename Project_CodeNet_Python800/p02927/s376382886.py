m, d = map(int, input().split())
ans = 0

for i in range(4, m + 1):
    for j in range(22, d + 1):
        d10 = j//10
        d1 = j%10
        if d10 >= 2 and d1 >= 2:
            if d10*d1 == i:
                ans += 1
print(ans)
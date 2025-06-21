m, d = list(map(int, input().split()))
ans = 0
for i in range(m+1):
    if i < 4:
        continue
    for j in range(d+1):
        d1 = j % 10
        d10 = j // 10
        if d1 <2 or d10 < 2:
            continue
        if d1 * d10 == i:
            ans += 1
print(ans)

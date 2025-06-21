[m,d] = [int(i) for i in input().split()]
ans = 0
for i in range(1,m+1):
    for j in range(1,d+1):
        da = str(j)
        if j < 10:
            d10 = 0
            d1 = da
        else:
            d10 = da[0]
            d1 = da[1]
        if int(d10) >= 2 and int(d1) >= 2 and int(d10) * int(d1) == i:
            ans += 1
print(ans)

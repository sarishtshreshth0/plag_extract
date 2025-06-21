M,D = map(int, input().split())
ans = 0
for i in range(1,M+1):
    for j in range(1,D+1):
        if j>= 22:
            d = str(j)
            d1 = int(d[1])
            d10 = int(d[0])
            if d1 * d10 == i and d1 >= 2:
                #print(d1,d10,i)
                ans += 1
print(ans)
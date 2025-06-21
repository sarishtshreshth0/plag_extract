m,d = map(int, input().split())
ans = 0



for i in range(m):
    i += 1
    for j in range(d):
        j += 1
        if j >= 22:
            r = str(j)
            a = int(r[0])
            b = int(r[1])
            if a >= 2 and b >= 2 and a*b == i:
                ans += 1

print(ans) 
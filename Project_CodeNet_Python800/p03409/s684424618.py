#091_C
n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]
cd = [tuple(map(int, input().split())) for _ in range(n)]

ab.sort(key = lambda x:(-x[1]))
cd.sort(key = lambda x:(x[0]))
flg = [True for _ in range(n)] 
ans = 0

for i in range(n):
    c, d = cd[i]
    for j in range(n):
        if flg[j]:
            a, b = ab[j]
            if a < c and b < d:
                ans += 1
                flg[j] = False
                break
                
print(ans)
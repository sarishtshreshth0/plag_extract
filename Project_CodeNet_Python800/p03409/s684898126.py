n = int(input())
ab = [tuple(map(int,input().split())) for i in range(n)]
cd = [tuple(map(int,input().split())) for i in range(n)]
ans = 0

ab = sorted(ab,key = lambda x:x[1],reverse = True)
cd.sort()



for (c,d) in cd:
    for (a,b) in ab:
        if a < c and b < d:
            ans += 1
            ab.remove((a,b))
            break
print(ans)

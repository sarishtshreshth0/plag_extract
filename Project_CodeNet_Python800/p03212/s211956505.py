from itertools import product as pro
n = int(input())
m = len(str(n))
ans = 0
for i in range(3,m+1):
    for l in pro([3,5,7],repeat=i):
        lst = list(l)
        x = ""
        for j in lst:
            x += str(j)
        if 3 in lst and 5 in lst and 7 in lst:
            if int(x) <= n:
                ans += 1
print(ans)
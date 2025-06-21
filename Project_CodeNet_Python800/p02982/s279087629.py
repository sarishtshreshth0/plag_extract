import math
N,D = map(int,input().split())
X = [[int(i) for i in input().split()] for _ in range(N)]
ans = 0
for i in range(N-1) :
    xi = X[i]
    for j in range(i+1,N) :
        xj = X[j]
        d2 = 0
        for k in range(D) :
            d2 += abs(xi[k]-xj[k])**2
        d = int(math.sqrt(d2))
        if d ** 2 == d2 :
            ans += 1

print(ans)
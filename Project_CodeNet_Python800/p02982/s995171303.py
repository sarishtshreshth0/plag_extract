N,D = map(int,input().split())
X = [tuple(map(int,input().split())) for i in range(N)]

ans = 0
for i,a in enumerate(X[:-1]):
    for b in X[i+1:]:
        d = 0
        for x,y in zip(a,b):
            d += (x-y)**2
        if d**0.5 - int(d**0.5) < 10e-10:
            ans += 1
print(ans)

N, M = map(int,input().split())
X = sorted(list(map(int,input().split())))

ans = sorted([X[x+1] - X[x] for x in range(M-1)])

if N >= M:
    print(0)
else:
    print(sum(ans[:M-N]))
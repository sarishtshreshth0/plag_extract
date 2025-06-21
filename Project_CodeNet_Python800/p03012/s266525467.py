N = int(input())
W = list(map(int,input().split()))
p = sum(W)
q = 0
for i in range(N):
    q += W[i]
    if q >= p/2:
        print(min(abs(p-2*sum(W[:i])),abs(p-2*sum(W[:i+1]))))
        exit()
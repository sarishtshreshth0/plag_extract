N = int(input())
W = list(map(int,input().split()))
m = sum(W)

for j in range(N-1):
    W1 = W[:j+1]
    W2 = W[j+1:N]
    s = abs(sum(W1) - sum(W2))
    m = min(m, s)

print(m)

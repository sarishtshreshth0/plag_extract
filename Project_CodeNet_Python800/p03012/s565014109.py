N = int(input())
W = list(map(int, input().split()))

R = sum(W) - W[0]
L = W[0]
S = []
for i in range(1,N):
    S.append(abs(R - L))
    R -= W[i]
    L += W[i]

print(min(S))
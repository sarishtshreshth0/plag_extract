N = int(input())
W = list(map(int, input().split()))

S1 = 0
S2 = sum(W)
min_diff = 100000
for i in range(1, N):
    S1 += W[i-1]
    S2 -= W[i-1]
    diff = abs(S2-S1)
    min_diff = min(diff, min_diff)
print(min_diff)

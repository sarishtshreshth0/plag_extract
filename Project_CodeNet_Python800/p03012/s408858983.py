N = int(input())
W = list(map(int, input().split()))

S1 = 0
S2 = sum(W)
ans = float("inf")
for w in W:
    S1 += w
    S2 -= w
    ans = min(ans, abs(S1 - S2))
print(ans)
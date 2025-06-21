N = int(input())
W = list(map(int,input().split()))

ans = sum(W)

L, R = sum(W), 0
for w in W:
    L -= w
    R += w
    ans = min(ans, abs(R-L))

print(ans)
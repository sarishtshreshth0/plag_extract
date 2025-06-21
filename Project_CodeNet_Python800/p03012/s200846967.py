N = int(input())
W = list(map(int, input().split()))

minw = sum(W)

for t in range(N):
    s1 = sum(W[:t])
    s2 = sum(W[t:])
    diff = abs(s1 - s2)
    minw = min(minw, diff)

print(minw)

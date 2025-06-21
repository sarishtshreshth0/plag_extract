N = int(input())
W = list(map(int, input().split()))
ans = 10**9
for i in range(N - 1):
    s1 = W[:i + 1]
    s2 = W[i + 1:]
    diff = abs(sum(s1) - sum(s2))
    if diff < ans:
        ans = diff
print(ans)

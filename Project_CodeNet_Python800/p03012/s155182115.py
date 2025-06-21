n = int(input())
w = list(map(int, input().split()))

ans = sum(w)
for t in range(0, n - 1):
    s1 = sum(w[0:t + 1])
    s2 = sum(w[t + 1:n])
    ans = min(ans, abs(s2 - s1))
print(ans)

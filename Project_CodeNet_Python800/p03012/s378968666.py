n = int(input())
w = [int(i) for i in input().split()]
ans = float('inf')
for i in range(n - 1):
    ans = min(ans, abs(sum(w[:i + 1]) - sum(w[i + 1:])))
print(ans)
n = int(input())
w = list(map(int, input().split()))
left, right = w[0], sum(w[1:])
ans = abs(left - right)
for i in range(1, n - 1):
    left += w[i]
    right -= w[i]
    ans = min(ans, abs(left - right))
print(ans)

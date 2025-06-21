n = int(input())
w = list(map(int, input().split()))
sum_w = sum(w)
total = 0
ans = 1000
for i in range(n):
    total += w[i]
    ans = min(ans, abs(sum_w - 2 * total))
print(ans)

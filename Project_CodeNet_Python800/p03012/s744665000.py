n = int(input())
w = list(map(int, input().split()))
sum_w = sum(w)
ans = 100000

t = 0
for i in range(n):
    t += w[i]
    ans = min(ans, abs(sum_w - 2*t))
print(ans)

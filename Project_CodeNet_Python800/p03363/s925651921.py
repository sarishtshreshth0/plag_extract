from collections import defaultdict
n = int(input())
a = list(map(int,input().split()))

ruisekiwa = [0 for _ in range(n+1)]
for i in range(n):
	ruisekiwa[i+1] = ruisekiwa[i] + a[i]

dp = defaultdict(lambda: 0)
ans = 0
for i in ruisekiwa:
	ans += dp[i]
	dp[i] += 1
print(ans)
n = int(input())
a = list(map(int, input().split()))
if a[0] > 0 or a.count(0) > 1:
  print(0)
  exit()
  
a = sorted(a)
dp = [0]*(n+1)
dp[0] = 1
count_list = [0]*n
count_list[0] = 1
for i in range(1, n):
  count_list[a[i]] += 1
for i in range(1, a[n-1]+1):
  dp[i] = dp[i-1] * count_list[i-1] ** count_list[i] % 998244353
print(dp[a[n-1]])
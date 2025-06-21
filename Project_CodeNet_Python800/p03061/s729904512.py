from fractions import gcd
n = int(input())
a = list(map(int,input().split()))
GCD= a[0]
dp = [set() for i in range(n)]
dp[1].add(a[0])
dp[1].add(a[1])
for i in range(1,n):
    x = a[i]
    for j in dp[i-1]:
            dp[i].add(gcd(j,x))
    if x % GCD != 0:
        dp[i].add(GCD)
        GCD = gcd(GCD,x)
print(max(dp[n-1]))

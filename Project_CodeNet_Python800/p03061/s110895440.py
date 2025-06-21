n = int(input())
As = list(map(int, input().split()))
# from math import gcd
def gcd(n, m):
    # 最大公約数
    a = max(n,m)
    b = min(n,m)
    while b:
        a, b = b, a % b
    return a
# 左からの累積GCDと
g = As[0]
left = []
for a in As:
    g = gcd(g, a)
    left.append(g)
# 右からの累積GCD
As_r = As[::-1]
g_r = As_r[0]
right = []    
for a in As_r:
    g_r = gcd(g_r, a)
    right.append(g_r)
    
l = left
r = right[::-1]
ans = 0
for i in range(n):
    if i == 0:
        ans = max(ans, r[1])
    elif i == n-1:
        ans = max(ans, l[n-2])
    else:     
        g = gcd(l[i-1],r[i+1])
        ans = max(ans, g)
print(ans)
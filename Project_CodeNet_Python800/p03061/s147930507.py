from fractions import gcd
n = int(input())
a = list(map(int, input().split()))
gcd_l = a[0]
gcd_r = a[-1]
gcd_l_li = []
gcd_r_li = []
for i in range(n):
    gcd_l = gcd(gcd_l, a[i])
    gcd_l_li.append(gcd_l)
for i in range(n)[::-1]:
    gcd_r = gcd(gcd_r, a[i])
    gcd_r_li.append(gcd_r)
#print(gcd_l_li)
#print(gcd_r_li)

ans = max(gcd_r_li[n-2], gcd_l_li[n-2])  # かきかえる整数が右端のときと左端のとき
for target in range(1, n-1):
    ans = max(ans, gcd(gcd_l_li[target-1], gcd_r_li[n-2-target]))
print(ans)



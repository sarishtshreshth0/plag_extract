import math

n = int(input())
a = list(map(int,input().split()))
a.sort()

fo = [a[0]]
re = [a[-1]]

x,y = a[0] , a[-1]
for i in range(n-1):
    x = math.gcd(x,a[i+1])
    y = math.gcd(y,a[n-2-i])
    fo.append(x)
    re.append(y)
    
ans = re[n-2]
for i in range(1,n-1):
    ans = max(ans , math.gcd(fo[i-1],re[n-2-i]))
ans = max(ans , fo[n-2])

print(ans)
import math
[n,x] = [int(i) for i in input().split()]
xs = [int(i) for i in input().split()]
if n != 1:
    xs.append(x)
    xs.sort()
    diff = []
    for i in range(1,n+1):
        diff.append(xs[i] - xs[i-1])
    ans = 0
    for i in range(1,len(diff)):
        if i == 1:
            ans = math.gcd(diff[i-1],diff[i])
        else:
            ans = math.gcd(ans,diff[i])
    print(ans)
else:
    print(abs(x - xs[0]))

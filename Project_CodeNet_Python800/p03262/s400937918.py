from math import gcd

n,x = map(int,input().split())
c = list(map(int,input().split()))
c.append(x)
c.sort()
arr = []
for i in range(n):
    arr.append(abs(c[i]-c[i+1]))
ans = arr[0]
if n>1:
    ans = gcd(arr[0],arr[1])
    for i in range(2,n):
        ans = gcd(ans,arr[i])
print(ans)
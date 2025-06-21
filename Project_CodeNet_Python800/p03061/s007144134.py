from fractions import gcd
n = int(input())
a = list(map(int,input().split()))
left = []
right = []

left.append(a[0])
for i in range(1,n-1):
    left.append(gcd(left[-1],a[i]))
a = a[::-1]
right.append(a[0])
for i in range(1,n-1):
    right.append(gcd(right[-1],a[i]))
ans = 1
for i in range(n-1):
    ans = max(ans,gcd(left[i],right[n-i-3]))
ans = max(ans,left[n-2],right[n-2])
print(ans)

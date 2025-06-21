from collections import Counter
n=int(input())
a=list(map(int,input().split()))
s=[0]*(n+1)
for i in range(n):
    s[i+1] = s[i] + a[i]
c = Counter(s)
n = set(s)
ans = 0
for i in n:
    ans += ((c[i]*(c[i]-1))//2)
print(ans)
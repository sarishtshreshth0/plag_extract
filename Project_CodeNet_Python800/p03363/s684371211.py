from collections import Counter
n = int(input())
a = list(map(int,input().split()))
s = [0]*(n+1)
def C(x):
    return x*(x-1)//2
for i in range(n):
    s[i+1] = s[i]+a[i]
c = Counter(s)
ans = 0
for v in c.values():
    ans += C(v)
print(ans)
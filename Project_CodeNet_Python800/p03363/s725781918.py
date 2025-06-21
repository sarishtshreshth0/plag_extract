from collections import Counter
n = int(input())
a = list(map(int, input().split()))
a1 = [0]*(n+1)

for i in range(n):
    a1[i+1] = a1[i]+a[i]

ans = 0
c = Counter(a1)
for i in c.values():
    ans += i*(i-1)//2
print(ans)

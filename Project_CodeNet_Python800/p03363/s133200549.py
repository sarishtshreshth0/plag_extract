from collections import Counter
n = int(input())
a = list(map(int, input().split()))
cum = [0] 
for i in range(n):
    cum.append(cum[i] + a[i])
c = Counter(cum)
ans = 0
for v in c.values():
    ans += v * (v - 1)// 2
print(ans)
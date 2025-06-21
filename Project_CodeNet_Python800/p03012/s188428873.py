n = int(input())
a = list(map(int,input().split()))
s = []
tmp = 0
for i in range(n-1):
    tmp += a[i]
    s.append(tmp)

ans = 10**9
total = sum(a)
for i in s:
    ans = min(ans, abs(total-2*i))
print(ans)
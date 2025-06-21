n = int(input())
a = list(map(int, input().split()))
c = [0]*(n+1)
for i in a:
  c[i] += 1
ans = 1
for i in range(n+1):
    if c[-1] == 0:
        c.pop()
    else:
        break

mod = 998244353
for i in range(len(c)-1):
    ans *= pow(c[i], c[i+1], mod)
    ans %= mod

if a[0] != 0:
    ans *= 0
if c[0] != 1:
    ans *= 0
print(ans)

n,a,b = map(int,input().split())
mod = 10**9 + 7
all = pow(2, n, mod)
if all == 0:
    all = 10**9 + 6
else:
    all -= 1

a = min(n-a,a)
b = min(n-b,b)

a_fact = 1
a_inv = 1
for i in range(1,a+1):
    a_fact *= (n-i+1)%mod
    a_inv *= pow(i,mod-2,mod)
    a_fact %= mod
    a_inv %= mod
nca = a_fact * a_inv
nca %= mod

b_fact = 1
b_inv = 1
for i in range(1,b+1):
    b_fact *= (n-i+1)%mod
    b_inv *= pow(i,mod-2,mod)
    b_fact %= mod
    b_inv %= mod
ncb = b_fact * b_inv
ncb %= mod

ans = all - nca - ncb

while ans < 0:
    ans += mod
if ans >= mod:
    ans -= mod
print(ans)
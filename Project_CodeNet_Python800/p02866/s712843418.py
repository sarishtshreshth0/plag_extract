mod = 998244353
N = int(input())
D = [int(i) for i in input().split()]
if D[0] != 0:
    print(0)
    exit()
for i in range(1,N):
    if D[i] == 0:
        print(0)
        exit()
def pow_k(a,n,mod): #a**n
    if n == 0:
        return 1
    if n % 2 ==0:
        return pow_k(a*a % mod,n//2,mod)
    else:
        return a * pow_k(a,n-1,mod) % mod
import collections
c = collections.Counter(D)
li = list(c.keys())
li.sort()
n = li[-1]
ans = 1
for i in range(1,n+1):
    if c[i] == 0:
        print(0)
        exit()
    else:
        j = i-1
        k = pow_k(c[j],c[i],mod)
        ans *= k
        ans %= mod
print(ans)
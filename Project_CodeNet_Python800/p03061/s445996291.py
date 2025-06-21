from math import gcd
n = int(input())
a = list(map(int, input().split()))

pref = [0]; suff = [0]

for i in range(n):
    pref.append(gcd(pref[-1], a[i]))

for i in range(n-1, -1, -1):
    suff.append(gcd(suff[-1], a[i]))

suff.reverse()

ans = pref[-1]

for i in range(len(pref)-1):
    ans = max(ans, gcd(pref[i], suff[i+1]))

print(ans)
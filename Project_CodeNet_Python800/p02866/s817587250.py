from collections import Counter
n = int(input())
D = list(map(int,input().split()))
Dc = Counter(D)
mod = 998244353
ans = 1

if Dc[0]!=1 or D[0]!=0:
    print(0)
else:
    for i in range(max(D)):
        ans = ans*pow(Dc[i],Dc[i+1])%mod
    print(ans%mod)
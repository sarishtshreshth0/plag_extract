n=int(input())
d=list(map(int,input().split()))
if d[0] != 0:
    print(0)
    exit()
d.sort()
if d[1] == 0:
    print(0)
    exit()
cnt = 1
pre = 1
ans =1
i = 1
mod = 998244353
while i < n:
    if d[i]-1 != d[i-1]:
        ans = 0
    while i!=n-1 and d[i+1] == d[i]:
        i+=1
        cnt+=1
    ans *= pow(pre,cnt,mod)
    ans %= mod
    pre =cnt
    cnt = 1
    i+=1
print(ans)
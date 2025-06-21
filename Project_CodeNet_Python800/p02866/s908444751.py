from collections import Counter

n=int(input())
d=list(map(int,input().split()))
dic=Counter(d)
MOD=998244353
ans=1
if d[0]!=0 or dic[0]!=1: print(0)
else:
    for i in range(1,max(dic.keys())+1):
        ans*=pow(dic[i-1],dic[i],MOD)
        ans%=MOD
    print(ans)
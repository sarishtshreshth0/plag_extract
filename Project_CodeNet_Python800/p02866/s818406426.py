n=int(input())
l=list(map(int,input().split()))
if l[0]:print(0);exit()
mod=998244353
k=[0]*n
for i in l:k[i]+=1
if k[0]!=1:print(0);exit()
ans=1
for i,s in zip(k,k[1:]):ans*=pow(i,s,mod)
print(ans%mod)
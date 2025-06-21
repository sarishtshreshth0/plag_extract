N=int(input())
A=list(map(int,input().split()))
S=[0]
mp={0:1}
for i in range(N):
  S.append(S[-1]+A[i])
  mp[S[-1]]=mp.get(S[-1],0)+1
ans=0
for i in mp:
  ans+=mp[i]*(mp[i]-1)//2

print(ans)
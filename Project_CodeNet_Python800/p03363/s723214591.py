N=int(input())
A=list(map(int, input().split()))
D=[0]
d=0
for i in A:
  d+=i
  D.append(d)
D=sorted(D)
ans=0
d=-10**9+1
D.append(10**9+1)
cnt=0
for i in range(N+2):
  if D[i]==d:
    cnt+=1
  else:
    if cnt>1:
      ans+=cnt*(cnt-1)//2
      cnt=1
    else:
      cnt=1
    d=D[i]
print(ans)
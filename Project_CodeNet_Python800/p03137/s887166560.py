N,M=map(int,input().split())
R=[0]*(M-1)
L=list(map(int,input().split()))
L=sorted(L)
for i in range(M-1):
  R[i]=abs(L[i+1]-L[i])
c=max(L)-min(L)
R=sorted(R,reverse=True)
print(c-sum(R[:min(N-1,len(R))]))
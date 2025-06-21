N=int(input())
S=input()
R=[0 for i in range(N)]
L=[0 for i in range(N)]
LL=0
RR=0
for i in range(N):
  if S[i]=='(':
    LL+=1
  else:
    RR+=1
  L[i]=LL
  R[i]=RR
s=0
for i in range(N):
  s=max(s,R[i]-L[i])
t=s+L[N-1]-R[N-1]
print('('*s+S+')'*t)
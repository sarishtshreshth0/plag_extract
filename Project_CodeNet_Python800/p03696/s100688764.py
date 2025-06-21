N=int(input())
X=0
S=input()
T,U='',''
for i in range(N):
  if S[i]=='(':
    X+=1
  else:
    if X==0:
      T+='('
    else:
      X-=1
U=')'*X
print(T+S+U)
N=int(input())
S=input()
x, y, z=0, 0, 0
for i in range(N):
  if S[i]=='(':
    x+=1
  else:
    y+=1
  z=min(z, x-y)
print('('*-z+S+')'*max(0, x-z-y))
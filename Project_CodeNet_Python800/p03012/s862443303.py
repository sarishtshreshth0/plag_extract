N=int(input())
W=list(map(int,input().split()))
t=sum(W)
a=[]
for x in range(N):
  s1=0
  for y in range(x+1):
    s1 += W[y]
  a.append(abs(t-2*s1))
print(min(a))
N=int(input())
L=list(map(int, input().split()))
s=sum(L)
A=[]
for i in range(N+1):
  t=sum(L[:i])
  A.append(abs(t-(s-t)))
print(min(A))
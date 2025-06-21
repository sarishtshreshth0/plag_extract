mina=10**10
a=int(input())
L=list(map(int,input().split()))
c=sum(L)
for i in range(a):
  d=c-sum(L[:i+1])
  mina=min(mina,abs(d-sum(L[:i+1])))
print(mina)
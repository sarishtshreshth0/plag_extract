def check(n,k):
  r=[]
  while n>0:
    r.append(n%k)
    n//=k
  return len(r)
n,k=map(int,input().split())
print(check(n,k))
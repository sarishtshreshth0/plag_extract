n=int(input())
w=list(map(int,input().split()))
ans=10000

for i in range(n):
  s1=0
  s2=0
  for j in range(i):
    s1=s1+w[j]
  for k in range(i, n):
    s2=s2+w[k]
  ans=min(ans, max(s1, s2)- min(s1, s2))
  
print(ans)
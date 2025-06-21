n=int(input())
w=list(map(int,input().split()))
z=100
for i in range(n):
  s1=0
  s2=0
  for j in range(i+1):
    s1+=w[j]
  for k in range((n-i)-1):
    s2+=w[-(k+1)]
  if z>abs(s1-s2):
    z=abs(s1-s2)
print(z)
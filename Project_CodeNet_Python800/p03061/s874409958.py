n=int(input())
a=list(map(int,input().split()))
def gcd(a, b):
  while b:
    a, b = b, a%b
  return a
al=[]
ar=[]
tmp=a[0]
al.append(a[0])
for ai in a[1:]:
  tmp=gcd(ai,tmp)
  al.append(tmp)
ar.append(a[-1])
tmp=a[-1]
for ai in a[:-1][::-1]:
  tmp=gcd(ai,tmp)
  ar.append(tmp)
ans=ar[n-2]
for i in range(n-1):
  ans=max(ans,gcd(al[i],ar[n-i-3]))
ans=max(ans,al[n-2])
print(ans)


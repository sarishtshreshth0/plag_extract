def gcd(a,b):
  if b == 0:
    return a
  else:
    return gcd(b,a%b)    

n,ans=int(input()),1
A=list(map(int,input().split()))
gcd_l,gcd_r=[],[]
l,r=A[0],A[n-1]

for i in range(n-1):
  l,r=gcd(l,A[i]),gcd(r,A[n-i-1])
  gcd_l.append(l)
  gcd_r.append(r)

for i in range(n-2):
  v=gcd(gcd_l[i],gcd_r[n-3-i])
  if v > ans:
    ans = v

if gcd_l[n-2] > ans:
  ans=gcd_l[n-2]
if gcd_r[n-2] > ans:
  ans=gcd_r[n-2]
  
print(ans)
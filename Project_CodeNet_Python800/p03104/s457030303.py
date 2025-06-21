a,b=map(int,input().split())
def func(n,m):# 0<=i<=mのiを二進数表示した時、2^nのくらいが1となるiの個数。のiで(i//2^n)%2=1となるiの個数<=>i//2^nが奇数
  c=m//pow(2,n)
  d=m%pow(2,n)
  # m=c*pow(2,n)+d
  if c%2==0:
    return pow(2,n)*(c//2)
  else:
    return pow(2,n)*((c-1)//2)+d+1
i=0
while pow(2,i)<=b:
  i+=1
maxn=i
ans=0
for i in range(maxn+1):
  e=func(i,b)-func(i,max(0,a-1))
  if e%2==1:
    ans+=pow(2,i)
print(ans)

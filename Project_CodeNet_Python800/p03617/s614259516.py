q,h,s,d=map(int,input().split())
n=int(input())

a,b,c=q*8,h*4,s*2

x=n//2

ans=0

ans+=x*min(a,b,c,d)

if n%2==1:
  ans+=min(a//2,b//2,c//2)
  
print(ans)
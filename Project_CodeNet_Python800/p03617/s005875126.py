q,h,s,d=map(int,input().split())
n=int(input())
List1=[q*4,h*2,s]
List2=[q*8,h*4,s*2,d]
if (n%2==0):
  ans=n*min(List2)//2
  print(ans)
else:
  ans=(n-1)*min(List2)//2
  ans+=min(List1)
  print(ans)
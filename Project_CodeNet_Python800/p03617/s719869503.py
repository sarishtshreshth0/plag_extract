a,b,c,d=map(int,input().split())
n=int(input())
if n == 1:
  print(min(a*4,b*2,c))
elif n%2 == 0:
  print(min(a*4*n,b*2*n,c*n,d*n//2))
else:
  print(min(a*4*n,b*2*n,c*n,n//2*d+min(a*4,b*2,c)))

q,h,s,d=map(int,input().split())
n=int(input())
if n==1:
  print(min(s,h*2,q*4))
elif n%2==0:
  print(min(int(n/2)*d,n*s,2*n*h,4*n*q))
else:
  print(min(int(n/2)*d+s,int(n/2)*d+2*h,int(n/2)*d+4*q,n*s,2*n*h,4*n*q))
q,h,s,d=map(int,input().split())
n=int(input())
n*=4
j=4*(2*q<h)+2*(2*h<s)+(4*q<s)
if j%4==0:
  if 2*s<d:
    print(s*(n//4))
  else:
    print(d*(n//8)+s*((n%8)//4))
  
if j==2 or j==3:
  if 4*h<d:
    print(h*(n//2))
  else:
    print(d*(n//8)+h*((n%8)//2))

if j==5 or j==7:
  if q*8<d:
    print(q*n)
  else:
    print(d*(n//8)+q*(n%8))
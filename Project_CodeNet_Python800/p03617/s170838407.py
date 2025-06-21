q,h,s,d=map(int,input().split())
n=int(input())
cost=0
if n>=2:
    cost+=n//2*min(q*8,h*4,s*2,d)
    n%=2
if n>=1:
    cost+=n//1*min(q*4,h*2,s)
    n%=1
if n>=0.5:
    cost+=n//0.5*min(q*2,h)
    n%=0.5
if n>=0.25:
    cost+=n//0.25*q
print(cost)
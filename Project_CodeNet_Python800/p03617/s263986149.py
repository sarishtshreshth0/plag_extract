q,h,s,d=map(int,input().split())
n=int(input())
unit=min(q*4,h*2,s)

if n%2==0:
    print(min(unit*n,d*(n//2)))
else:
    print(min(unit*n,d*(n//2)+unit))


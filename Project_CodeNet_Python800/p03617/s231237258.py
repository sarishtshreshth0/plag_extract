q,h,s,d=map(int,input().split())
n=int(input())
q*=4
h*=2
if n%2==0:
    print(min(min(q,h,s)*n,d*n//2))
else:
    print(min(min(q,h,s)*n,d*(n//2)+min(q,h,s)))
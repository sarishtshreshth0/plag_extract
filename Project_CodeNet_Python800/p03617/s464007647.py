from decimal import Decimal as de
q,h,s,d=map(de,input().split())
n=de(input())
ans=0

if n%2:
    ans+=min(4*q,2*h,s)
    n-=1
print(int((ans+n*min(4*q,2*h,s,d/2))//1))
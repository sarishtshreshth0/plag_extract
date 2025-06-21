q,h,s,d=map(int,input().split())
n=int(input())
ans=0
a=min(4*q,2*h,s)
b=min(2*a,d)

print((n%2)*a+(n//2)*b)
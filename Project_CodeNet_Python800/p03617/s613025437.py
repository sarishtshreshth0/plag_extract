q,h,s,d=map(int,input().split())
n=int(input())
Q=4*q
H=2*h
S=s
D=d/2
b=[Q,H,S,D]
a=sorted(b)
if a[0]==D and n%2==1:
    ans=(n//2)*d+a[1]
elif a[0]==D:
    ans=(n//2)*d
else:
    ans=n*a[0]
print(ans)
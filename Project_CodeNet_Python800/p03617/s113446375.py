#AtCoder Grand Contest 019 a
q,h,s,d=map(int,input().split())#0.25,0.5,1,2
d=min(d,s*2,h*4,q*8)
s=min(s,h*2,q*4)

n=int(input())
if n%2==0:
    print(n//2*d)
else:
    print(n//2*d+s)

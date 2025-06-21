q,h,s,d=map(int, input().split())
n = int(input())
q*=4
h*=2
t = min(q, h, s)
ans=0
while n!=0:
    if n==1:
        ans+=t
        break
    if n%2==1:
        if 2*t < d:
            ans+=2*t*(n-1)//2
            n=1
        else:
            ans+=d*(n-1)//2
            n=1
    else:
        if 2*t < d:
            ans+=t*(n)
            n=0
        else:
            ans+=d*(n)//2
            n=0

print(ans)

Q,H,S,D=map(int,input().split())
N=int(input())

q=Q*8
h=H*4
s=S*2
d=D
if N%2==0:
    ans=(N//2)*min(q,h,s,d)
    print(ans)
else:
    ans=(N//2)*min(q,h,s,d)
    q=Q*4
    h=H*2
    s=S
    ans+=min(q,h,s)
    print(ans)
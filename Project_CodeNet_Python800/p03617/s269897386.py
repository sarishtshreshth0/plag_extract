Q, H, S,D = map(int,input().split())
N=int(input())

L=min(4*Q, 2*H,S)
if 2*L<=D:
    ans=N*L
else:
    m=N//2
    ans=m*D+L*(N-2*m)
    
print(ans)
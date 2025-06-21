Q,H,S,D=map(int,input().split())
N=int(input())

ans=0
p=min(Q*8,H*4,S*2,D)
q=N
ans=p*(q//2)

p=min(Q*4,H*2,S)
q=q%2
ans+=p*(q//1)

print(int(ans))
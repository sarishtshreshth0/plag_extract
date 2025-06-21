Q,H,S,D=list(map(int,input().split()))
N=int(input())
ans=0
min_tea=min(Q*8,H*4,S*2,D)
ans+= (N//2) * min_tea
N-=(N//2)*2
min_tea=min(Q*4,H*2,S*1)
ans+= (N//1) * min_tea
print(ans)
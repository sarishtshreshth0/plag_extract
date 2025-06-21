Q,H,S,D = map(int,input().split())
N = int(input())
a2 = min(Q*8,H*4,S*2,D)
ans = (N//2)*a2
a1 = min(Q*4,H*2,S)
ans += (N%2)*a1
print(ans)
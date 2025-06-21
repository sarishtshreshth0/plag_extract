Q,H,S,D = map(int, input().split())
N = int(input())
ans = 0
si = min(Q*4, H*2, S)
db = min(si*2, D)
ans = (N%2)*si + (N//2)*db
print(ans)
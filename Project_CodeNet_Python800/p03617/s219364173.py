Q, H, S, D = map(int, input().split())
N = int(input())

if N == 1:
    ans = min(Q*4, H*2, S)
else:
    n = N // 2
    ans = min(Q*8, H*4, S*2, D)
    ans *= n
    if N % 2 == 1:
        ans += min(Q*4, H*2, S)

print(ans)
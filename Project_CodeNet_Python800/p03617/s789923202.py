Q, H, S, D = map(int, input().split())
N = int(input())
r = 0
if D*1<=Q*8 and D*1<=H*4 and D*1<=S*2:
    r += (N//2)*D
    N = N % 2

if S*2 <= H*4 and S*2 <= Q*8:
    r += N*S
    N = 0
if H*4 <= S*2 and H*4 <= Q*8:
    r += N*H*2
    N = 0
if Q*8 <= S*2 and Q*8 <= H*4:
    r += N*Q*4
    N = 0

print(r)

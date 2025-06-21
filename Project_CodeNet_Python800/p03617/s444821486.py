Q, H, S, D = map(int, input().split())
N = int(input())

if N % 2 == 0:
    Min = min(N*Q*4, N*H*2, N*S, N//2*D)
else:
    Min = min((N-1)*Q*4, (N-1)*H*2, (N-1)*S, N//2*D) + min(4*Q, 2*H, S)
print(Min)
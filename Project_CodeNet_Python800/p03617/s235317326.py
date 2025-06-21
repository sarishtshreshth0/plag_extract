Q, H, S, D = map(int, input().split())
N = int(input())
ans = 0
if N % 2 == 0:
    ans = min(4*N*Q, 2*N*H, N*S, N*D//2)
else:
    ans += min(4*(N-1)*Q, 2*(N-1)*H, (N-1)*S, (N-1)*D//2)
    ans += min(4*Q, 2*H, S)

print(ans)
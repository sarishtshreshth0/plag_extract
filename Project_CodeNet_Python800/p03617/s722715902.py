Q, H, S, D = map(int, input().split())
N = int(input())
n = N//2
ans = min(D, 2*S, 4*H, 8*Q)*n + min(S, 2*H, 4*Q)*(N%2)
print(ans)
Q, H, S, D = map(int, input().split())
N = int(input())
n = N // 2 * 2
ans =  min(n * Q * 4, n * H * 2, n * S, n * D // 2)
if N % 2 == 1:
    ans += min(Q * 4, H * 2, S)
print(ans)
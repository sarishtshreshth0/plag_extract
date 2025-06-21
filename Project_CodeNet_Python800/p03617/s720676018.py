Q, H, S, D = map(int, input().split())
N = int(input()) * 4
A = [Q, min(2 * Q, H), min(4 * Q, 2 * H, S), min(8 * Q, 4 * H, 2 * S, D)]
ans = (N // 8) * A[3] + ((N % 8) // 4) * A[2] + ((N % 4) // 2) * A[1] + (N % 2) * A[0]
print(ans)
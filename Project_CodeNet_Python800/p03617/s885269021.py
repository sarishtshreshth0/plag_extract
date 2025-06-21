Q, H, S, D = map(int, input().split())
N = int(input())
single = min(Q * 4, H * 2, S)
print(min(single * N, N // 2 * D + N % 2 * single))
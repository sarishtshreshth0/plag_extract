Q, H, S, D = map(int, input().split())
N = int(input())

new_S = min(2 * min(2 * Q, H), S)
if 2 * new_S >= D:
    q, r = divmod(N, 2)
    print(q * D + r * new_S)
else:
    print(N * new_S)

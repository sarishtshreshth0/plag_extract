Q, H, S, D = [int(_) for _ in input().split()]
N = int(input())

H = min(H, Q*2)
S = min(S, H*2)
D = min(D, S*2)

if N % 2 == 0:
    print(D * (N // 2))
else:
    print(D * (N // 2) + S)

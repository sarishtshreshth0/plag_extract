Q, H, S, D = map(int, input().split())
N = int(input())

cQ = Q*8
cH = H*4
cS = S*2
cD = D 

m = min(cQ, cH, cS, cD)

if m == cQ:
    print(Q * N * 4)
elif m == cH:
    print(H * N * 2)
elif m == cS:
    print(S * N)
else:
    if N % 2 == 0:
        print(D * N // 2)
    elif N == 1:
        print(min(Q * 4, H * 2, S))
    else:
        c = (N-1) // 2 * D
        print(c + min(Q * 4, H * 2, S))

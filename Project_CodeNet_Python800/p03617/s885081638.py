def resolve():
    # import sys
    # input = sys.stdin.readline
    Q, H, S, D = [int(i) for i in input().split()]
    N = int(input())
    a = []
    a.append(N * S)
    a.append(N * H * 2)
    a.append(N * Q * 4)
    if N > 1:
        if N % 2 == 0:
            a.append((N // 2) * D)
        else:
            a.append((N // 2) * D + S)
            a.append((N // 2) * D + H * 2)
            a.append((N // 2) * D + Q * 4)
    print(min(a))


resolve()

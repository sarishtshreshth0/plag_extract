def resolve():
    # 整数 1 つ
    # n = int(input())
    # 整数複数個
    a, b, c, d = map(int, input().split())
    # 整数 N 個 (改行区切り)
    # N = [int(input()) for i in range(N)]
    # 整数 N 個 (スペース区切り)
    # N = list(map(int, input().split()))
    # 整数 (縦 H 横 W の行列)
    # A = [list(map(int, input().split())) for i in range(H)]

    A = [i for i in range(a, b+1)]
    B = [i for i in range(c, d+1)]

    cnt = 0
    for a in A:
        for b in B:
            if a == b:
                cnt += 1
                break

    if cnt == 0:
        print(cnt)
    else:
        print(cnt -1)


resolve()
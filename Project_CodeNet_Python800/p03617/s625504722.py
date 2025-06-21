def resolve():
    Q, H, S, D = list(map(int, input().split()))
    N = int(input())
    ans = 0

    ls = [[0.25, Q, 8*Q, 0], [0.5, H, 4*H, 0], [1, S, 2*S, 0], [2, D, D, 0]]
    ls.sort(key=lambda x: x[2])

    for i in range(4):
        if N < ls[i][0]:
            continue

        ls[i][3] += int(N // ls[i][0])
        N -= ls[i][0] * ls[i][3]

        ans += ls[i][1] * ls[i][3]

    ans = int(ans)
    print(ans)
    return


resolve()
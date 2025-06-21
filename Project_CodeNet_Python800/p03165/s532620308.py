def solve():
    Ss = input().rstrip()
    Ts = input().rstrip()

    lenS, lenT = len(Ss), len(Ts)

    dp = [[0]*(lenT+1) for _ in range(lenS+1)]
    for iS, S in enumerate(Ss, start=1):
        dp0 = dp[iS-1]
        dpi = dp[iS]
        for jT, T in enumerate(Ts, start=1):
            if S == T:
                dpi[jT] = dp0[jT-1] + 1
            else:
                dpi[jT] = dpi[jT-1]
                if dp0[jT] > dpi[jT]:
                    dpi[jT] = dp0[jT]

    anss = ''
    iS, jT = lenS, lenT
    while True:
        if Ss[iS-1] == Ts[jT-1]:
            anss += Ss[iS-1]
            iS, jT = iS-1, jT-1
        elif dp[iS-1][jT] >= dp[iS][jT-1]:
            iS -= 1
        else:
            jT -= 1
        if iS == 0 or jT == 0:
            break

    print(anss[::-1])


solve()

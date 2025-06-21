def solve():
    Q, H, S, D = [int(i) for i in input().split()]
    P = [(250, Q), (500, H), (1000, S), (2000, D)]
    P.sort(key=lambda t: t[1] / t[0])
    N = int(input()) * 1000
    ans = 0
    for p in P:
        if N == 0:
            break
        x, y = p
        n = int(N / x)
        ans += n * y
        N -= n * x
    print(ans)


if __name__ == "__main__":
    solve()

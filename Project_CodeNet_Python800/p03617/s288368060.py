def solve(Q, H, S, D, N):
    prices =[(int(0.25 * 4), Q),
             (int(0.5 * 4), H),
             (int(1.0 * 4), S),
             (int(2.0 * 4), D)]
    prices.sort(key=lambda x: x[1] / x[0])
    ans = 0
    N *= 4
    for p in prices:
        L = N // p[0]
        ans += L * p[1]
        N -= L * p[0]
    return ans


if __name__ == "__main__":
    Q, H, S, D = tuple(map(int, input().split(" ")))
    N = int(input())
    print(solve(Q, H, S, D, N))

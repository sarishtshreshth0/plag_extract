def main():
    Q, H, S, D = map(int, input().split())
    N = int(input())

    H = min(H, 2*Q)
    S = min(S, 2*H, 4*Q)
    D = min(D, 2*S, 4*H, 8*Q)

    cost = [
        [0.25, Q],
        [0.5, H],
        [1, S],
        [2, D]
    ]

    cost.sort(reverse = True, key = lambda x : x[0])

    ans = 0
    for c in cost:
        if N <= 0:
            break

        r, m = divmod(N, c[0])
        ans += r*c[1]
        N -= r*c[0]

    print(ans)

if __name__ == "__main__":
    main()
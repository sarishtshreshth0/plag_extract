# coding: utf-8

# https://atcoder.jp/contests/abc117


def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X = sorted(X)

    if N >= M:
        return 0

    if N == 1:
        return X[-1] - X[0]

    ds = [None] * (M-1)
    for i in range(M-1):
        ds[i] = [X[i+1] - X[i], i]

    ds_sort = sorted(ds, key=lambda x: x[0], reverse=True)
    jump = ds_sort[:N-1]
    jump = sorted(jump, key=lambda x: x[1])

    ans = 0
    j = 0
    for i in range(M-1):
        if j < len(jump) and i == jump[j][1]:
            j += 1
            continue

        ans += ds[i][0]

    return ans


print(main())

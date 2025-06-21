import collections


def main():
    n = int(input())
    D = list(map(int, input().split()))

    mod = 998244353

    if D[0] != 0:
        print(0)
        return

    cnt = collections.Counter(D)

    if cnt[0] > 1:
        print(0)
        return

    ans = 1

    for i in range(1, max(D)+1):
        if cnt[i - 1] == 1:
            continue
        ans *= cnt[i - 1] ** cnt[i] % mod
        ans %= mod

    print(ans)


if __name__ == '__main__':
    main()

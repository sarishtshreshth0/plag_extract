import math  # noqa
import bisect  # noqa
import queue  # noqa


if __name__ == '__main__':
    N = int(input())
    D = list(map(int, input().split()))

    # cnt[k] = v ... 深さkのノード数
    cnt = {}
    max_depth = 0
    for d in D:
        max_depth = max(max_depth, d)
        if d not in cnt:
            cnt[d] = 1
        else:
            cnt[d] += 1

    # 頂点1との距離が0になるノードは1つしか存在しない
    if D[0] != 0:
        print(0)
        exit(0)
    elif cnt[0] > 1:
        print(0)
        exit(0)

    ans = 1
    MOD = 998244353
    for i in range(0, max_depth):
        if (i not in cnt) or (i + 1 not in cnt):
            ans = 0
            break
        ans *= cnt[i] ** cnt[i + 1]
        ans %= MOD

    print(ans)

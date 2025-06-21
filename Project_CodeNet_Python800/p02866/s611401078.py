from collections import Counter


def solve(n, arr):
    if arr[0] != 0:
        return 0

    c = Counter(arr)

    if c[0] != 1:
        return 0

    for i in range(max(c) + 1):
        if i not in c:
            return 0

    c = list(c.items())
    c.sort()

    prev = 1
    ans = 1
    mod = 998244353

    for _, i in c[1:]:
        ans *= prev**i % mod
        ans %= mod
        prev = i

    return ans


n = int(input())
arr = list(map(int, input().split()))

print(solve(n, arr))
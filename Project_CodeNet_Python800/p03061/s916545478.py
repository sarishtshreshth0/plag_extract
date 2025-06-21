from collections import Counter
from functools import lru_cache
from math import gcd


@lru_cache(maxsize=None)
def get_dividers(n):
    """
    正の整数 n の約数を取得する
    """

    dividers = {i for i in range(1, int(n ** 0.5) + 1) if n % i == 0}
    return dividers | {n // d for d in dividers}


@lru_cache(maxsize=None)
def lcm(a, b):
    """
    aとbの最小公倍数を計算する
    """

    return a * b // gcd(a, b)


N = int(input())
A = tuple(map(int, input().split(' ')))

counter = Counter()
for a in A:
    counter.update(get_dividers(a))

ans = 1
candidates = []
for key, value in counter.items():
    if value == N:
        ans = lcm(ans, key)
    elif value == N - 1:
        candidates.append(key)

if candidates:
    ans = max([lcm(ans, c) for c in candidates])

print(ans)

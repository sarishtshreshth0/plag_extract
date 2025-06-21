import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from itertools import accumulate
    from collections import Counter

    n = int(readline())
    a = list(map(int, readline().split()))
    counter = Counter()
    counter[0] += 1

    acc = list(accumulate(a))
    ans = 0

    for x in acc:
        ans += counter[x]
        counter[x] += 1

    print(ans)


if __name__ == '__main__':
    main()

import sys
from collections import Counter

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    counter = Counter()
    for a in A:
        counter[a - 1] += 1
        counter[a] += 1
        counter[a + 1] += 1

    ans = max(counter.values())

    print(ans)
    return


if __name__ == '__main__':
    main()

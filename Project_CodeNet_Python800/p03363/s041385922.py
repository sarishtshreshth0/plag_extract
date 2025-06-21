import sys
import collections

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    A = [int(x) for x in input().split()]

    ruiseki = [0] * (N + 1)
    for i, a in enumerate(A):
        ruiseki[i] = ruiseki[i - 1] + a

    c = collections.Counter(ruiseki)

    ans = 0
    for v in ruiseki:
        ans += c[v] - 1

    print(ans // 2)


if __name__ == '__main__':
    main()

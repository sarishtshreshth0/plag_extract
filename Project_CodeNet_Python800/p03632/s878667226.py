import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a, b, c, d = map(int, readline().split())

    ans = max(0, min(b, d) - max(a, c))

    print(ans)


if __name__ == '__main__':
    main()

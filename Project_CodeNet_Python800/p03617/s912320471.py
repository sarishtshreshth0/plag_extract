import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    q, h, s, d = map(int, readline().split())
    n = int(readline())
    ans = min(8 * q, 4 * h, 2 * s, d) * (n // 2) + min(4 * q, 2 * h, s) * (n % 2)
    print(ans)


if __name__ == '__main__':
    main()

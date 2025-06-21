import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K = map(int, read().split())

    ans = 0
    while N:
        N //= K
        ans += 1

    print(ans)
    return


if __name__ == '__main__':
    main()

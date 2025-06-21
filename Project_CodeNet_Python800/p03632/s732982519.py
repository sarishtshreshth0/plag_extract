import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A, B, C, D = map(int, readline().split())

    lower = max(A, C)
    upper = min(B, D)
    ans = max(upper - lower, 0)

    print(ans)
    return


if __name__ == '__main__':
    main()

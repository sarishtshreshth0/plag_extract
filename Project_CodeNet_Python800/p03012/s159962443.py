import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    N, *W = map(int, read().split())

    ans = INF
    for t in range(1, N):
        ans = min(ans, abs(sum(W[:t]) - sum(W[t:])))

    print(ans)
    return


if __name__ == '__main__':
    main()

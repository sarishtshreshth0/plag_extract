import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    W = [readline().strip() for _ in range(N)]

    for w in W:
        if W.count(w) > 1:
            print('No')
            return

    for i in range(N - 1):
        if W[i][-1] != W[i + 1][0]:
            print('No')
            return

    print('Yes')
    return


if __name__ == '__main__':
    main()

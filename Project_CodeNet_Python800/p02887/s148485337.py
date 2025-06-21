import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from itertools import groupby

    N = int(readline())
    S = input()
    ans = 0
    for g in groupby(S):
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()

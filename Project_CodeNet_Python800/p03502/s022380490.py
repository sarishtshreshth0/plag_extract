import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    S = input()
    N = int(S)

    f = 0
    for x in S:
        f += int(x)

    if N % f == 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()

import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, K = map(int, readline().split())

    digit = 0
    cur = 0

    while cur < N:
        digit += 1
        cur = K ** digit - 1

    print(digit)


if __name__ == '__main__':
    main()

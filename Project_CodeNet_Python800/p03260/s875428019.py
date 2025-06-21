import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    A, B = map(int, readline().split())

    if A % 2 == 1 and B % 2 == 1:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()

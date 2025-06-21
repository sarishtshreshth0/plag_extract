import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A, B = map(int, readline().split())
    if A == 1:
        A = 14
    if B == 1:
        B = 14

    if A > B:
        print('Alice')
    elif A < B:
        print('Bob')
    else:
        print('Draw')

    return


if __name__ == '__main__':
    main()

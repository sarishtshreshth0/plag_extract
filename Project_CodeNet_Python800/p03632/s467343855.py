import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A, B, C, D = map(int, readline().split())

    if B < C or D < A:
        ans = 0
    elif C > A:
        if D < B:
            ans = D - C
        else:
            ans = B - C
    else:
        if D < B:
            ans = D - A
        else:
            ans = B - A

    print(ans)
    return


if __name__ == '__main__':
    main()

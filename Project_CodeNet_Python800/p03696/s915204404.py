import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    S = readline().strip()

    left = right = 0
    for s in S:
        if s == '(':
            left += 1
        elif left > 0:
            left -= 1
        else:
            right += 1

    ans = '(' * right + S + ')' * left
    print(ans)

    return


if __name__ == '__main__':
    main()

import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())

    def rec(s):
        if int(s) > N:
            return 0
        ans = 0
        if all(c in s for c in '357'):
            ans += 1
        for c in '357':
            ans += rec(s + c)
        return ans

    ans = rec('0')
    print(ans)
    return


if __name__ == '__main__':
    main()

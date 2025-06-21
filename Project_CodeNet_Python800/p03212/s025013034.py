import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())

    def dfs(n, used):
        if n > N:
            return 0
        ans = 0
        if used == 7:
            ans += 1
        for i, d in enumerate((3, 5, 7)):
            ans += dfs(10 * n + d, used | (1 << i))
        return ans

    print(dfs(0, 0))
    return


if __name__ == '__main__':
    main()

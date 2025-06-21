import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())

    def rec(vec):
        if vec and int(''.join(vec)) > N:
            return 0
        ans = 0
        if all(c in vec for c in '357'):
            ans += 1
        for c in '357':
            vec.append(c)
            ans += rec(vec)
            vec.pop()
        return ans

    ans = rec([])
    print(ans)
    return


if __name__ == '__main__':
    main()

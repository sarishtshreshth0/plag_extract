import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A, B = map(int, readline().split())

    def f(x):
        r = (x + 1) % 4
        ans = 0
        for n in range(x, x - r, -1):
            ans ^= n
        return ans

    if A == 0:
        print(f(B))
    else:
        print(f(B) ^ f(A - 1))

    return


if __name__ == '__main__':
    main()

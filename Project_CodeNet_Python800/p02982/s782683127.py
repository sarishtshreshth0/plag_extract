import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    def calc(p, q):
        res = 0
        for i in range(D):
            res += (X[p][i] - X[q][i]) ** 2
        return res

    N, D = map(int, readline().split())
    X = []
    for _ in range(N):
        a = list(map(int, readline().split()))
        X.append(a)

    sq = set(x ** 2 for x in range(1000))
    
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            d = calc(i, j)
            if d in sq:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()

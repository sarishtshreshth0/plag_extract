import sys
from heapq import heappush, heappop

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, *AB = map(int, read().split())

    J = [[] for _ in range(M)]
    for a, b in zip(*[iter(AB)] * 2):
        if a > M:
            continue
        J[a - 1].append(b)

    hq = []
    ans = 0
    for i in range(M):
        for b in J[i]:
            heappush(hq, -b)
        if hq:
            ans += -heappop(hq)

    print(ans)
    return


if __name__ == '__main__':
    main()

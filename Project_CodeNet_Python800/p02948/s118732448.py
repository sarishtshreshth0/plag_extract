import sys
import heapq

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, M = map(int, input().split())
    d = {i: [] for i in range(M + 1)}
    for _ in range(N):
        a, b = map(int, input().split())
        if a > M:
            continue
        d[a].append(b)

    ans = 0
    q = []
    heapq.heapify(q)
    for i in range(M, 0, -1):
        a = M - i + 1
        for b in d[a]:
            heapq.heappush(q, -b)
        if q:
            b = heapq.heappop(q)
            ans += -b

    print(ans)


if __name__ == "__main__":
    main()

import sys
import heapq
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


def main():
    N, M = map(int, input().split())

    D = defaultdict(list)
    for i in range(N):
        A, B = map(int, input().split())
        D[A].append(-1 * B)
    R = []
    answer = 0
    for i in range(1, M + 1):
        if len(D[i]) > 0:
            d = D[i]
            for t in d:
                heapq.heappush(R, t)
        if R:
            answer += heapq.heappop(R)

    print(-1 * answer)


if __name__ == "__main__":
    main()

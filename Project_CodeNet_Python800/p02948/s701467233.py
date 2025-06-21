MOD = 10 ** 9 + 7
INF = 10 ** 11
import sys
sys.setrecursionlimit(100000000)
from heapq import heapify,heappop,heappush

def main():
    N,M = map(int,input().split())
    works = [tuple(map(int,input().split())) for _ in range(N)]
    works.sort(key = lambda x:x[0])
    q = []
    ans = 0
    j = 0
    for i in range(M):
        while j < N and works[j][0] <= i + 1:
            heappush(q,-works[j][1])
            j += 1
        if q:
            p = heappop(q)
            ans -= p
    print(ans)
if __name__ == '__main__':
    main()

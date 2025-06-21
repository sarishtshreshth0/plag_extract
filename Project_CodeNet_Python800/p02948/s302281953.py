import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()


def solve():
    N, M = map(int, input().split())
    AB = [[] for _ in range(M)]
    for i in range(N):
        a, b = map(int, input().split())
        if a <= M:
            AB[a - 1].append(b)

    for i in range(M):
        AB[i] = sorted(AB[i])

    # print(AB)

    reward = []
    heapq.heapify(reward)
    ans = 0
    for i in range(M):
        if AB[i]:
            r = (-1) * AB[i].pop(-1)
            heapq.heappush(reward, (r, i))
        if reward:
            r, ind = heapq.heappop(reward)
            ans += (-1) * r
            if AB[ind]:
                r = (-1) * AB[ind].pop(-1)
                heapq.heappush(reward, (r, ind))

    print(ans)


if __name__ == '__main__':
    solve()

import heapq
import sys


def main():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    jobs = [tuple(map(int, input().split())) for _ in range(n)]
    jobs.sort()

    ans = 0
    index = 0
    hq = []
    # 働くのは0からm-1日後
    for i in range(m - 1, -1, -1):
        while index < n and i + jobs[index][0] <= m:
            heapq.heappush(hq, -jobs[index][1])
            index += 1
            if index == n:
                break
        if not hq:
            continue
        ans -= heapq.heappop(hq)

    print(ans)


if __name__ == "__main__":
    main()

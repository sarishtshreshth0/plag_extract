from heapq import heappop, heapify, heappush


def main():
    n, m = map(int, input().split())
    work = [[] for _ in range(10 ** 5 + 1)]
    for _ in range(n):
        a, b = map(int, input().split())
        work[a].append(b)
    ans = 0
    q = []
    heapify(q)
    for i in range(1, m + 1):
        for w in work[i]:
            heappush(q, -w)
        if len(q) == 0:
            continue
        ans += heappop(q)
    ans *= -1
    print(ans)


if __name__ == '__main__':
    main()

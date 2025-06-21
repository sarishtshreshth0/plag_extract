import heapq


def main():
    n, m = [int(e) for e in input().split()]
    AB = [[int(e) for e in input().split()] for i in range(n)]

    AB.sort(key=lambda x: x[0])
    H = []
    ans = 0
    mi = 1
    for a, b in AB:
        while a > mi:
            if len(H) > 0:
                ans += -heapq.heappop(H)

            mi += 1
            if mi > m:
                break

        if a > m:
            break

        heapq.heappush(H, -b)

    while mi <= m and len(H) > 0:
        ans += -heapq.heappop(H)
        mi += 1

    print(ans)


if __name__ == '__main__':
    main()

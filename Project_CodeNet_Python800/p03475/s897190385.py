def main():
    from itertools import islice

    N = int(input())

    trains = []
    for _ in range(N - 1):
        c, s, f = map(int, input().split())
        trains.append((c, s, f))

    ans = []
    for i in range(N - 1):
        curr = 0
        for c, s, f in islice(trains, i, N - 1, 1):
            if curr < s: curr = s
            r = curr % f
            if r != 0: curr += f - r
            curr += c
        ans.append(curr)
    ans.append(0)

    print(*ans, sep='\n')


if __name__ == '__main__':
    main()

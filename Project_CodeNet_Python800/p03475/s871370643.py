def main():
    from itertools import islice

    N = int(input())

    trains = []
    for _ in range(N - 1):
        c, s, f = map(int, input().split())
        trains.append((c, s, f))

    ans = [0] * N
    for i, (ci, si, fi) in enumerate(trains):
        curr = si + ci
        for j, (cj, sj, fj) in enumerate(islice(trains, i + 1, N, 1)):
            if curr < sj: curr = sj
            r = curr % fj
            if r != 0: curr += (fj - r)
            curr += cj
        ans[i] = curr

    print(*ans, sep='\n')


if __name__ == '__main__':
    main()

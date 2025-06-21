def main():
    N = int(input())
    trains = [list(map(int, input().split(' '))) for _ in range(N - 1)]
    ans = [0 for _ in range(N)]
    for i in range(N - 1):
        t = 0
        for train in trains[i:]:
            c, s, f = train
            wait_time = s - t if t <= s else (f - t) % f
            t += wait_time + c
        ans[i] = t
    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
def main():
    N = int(input())
    d = [list(map(int, input().split())) for _ in range(N-1)]
    for i in range(N-1):
        measure_time(d[i], d[i+1:])
    print(0)


def measure_time(start, remain):
    t = 0
    t = start[1] + start[0]
    for r in remain:
        if t < r[1]:
            t = r[1]
        elif (t - r[1]) % r[2] != 0:
            t += r[2] - (t - r[1]) % r[2]
        t += r[0]
    print(t)


if __name__ == '__main__':
    main()

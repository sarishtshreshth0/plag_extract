def main():
    from math import ceil

    n, *csf = map(int, open(0).read().split())
    csf = list(zip(csf[::3], csf[1::3], csf[2::3]))
    times = []
    for i in range(n):
        time = 0
        for c, s, f in csf[i:]:
            g = time > s
            time = s + int(g) * ceil((time - s) / f) * f + c
        times.append(str(time))

    ans = "\n".join(times)
    print(ans)


if __name__ == '__main__':
    main()

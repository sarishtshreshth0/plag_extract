def main():
    from math import ceil

    n, *csf = map(int, open(0).read().split())
    csf = list(zip(csf[::3], csf[1::3], csf[2::3]))
    for i in range(n):
        time = 0
        for c, s, f in csf[i:]:
            if time <= s:
                time = s
            else:
                time = s + ceil((time - s) / f) * f
            time += c
        print(time)


if __name__ == '__main__':
    main()

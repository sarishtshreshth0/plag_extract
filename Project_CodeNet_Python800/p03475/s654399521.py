def main():
    from math import ceil

    n, *csf = map(int, open(0).read().split())
    csf = list(zip(csf[::3], csf[1::3], csf[2::3]))
    ans = ""
    for i in range(n):
        time = 0
        for c, s, f in csf[i:]:
            if time <= s:
                time = s + c
            else:
                time = s + ceil((time - s) / f) * f + c            

        ans += str(time) + '\n'
    print(ans)

if __name__ == '__main__':
    main()

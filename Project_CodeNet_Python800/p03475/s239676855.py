def main():
    n = int(input())
    csf = [tuple(map(int, input().split())) for _ in range(n - 1)]
    r = [0] * n
    for i1 in range(n - 1):
        t = 0
        for i2 in range(i1, n - 1):
            if t <= csf[i2][1]:
                t = csf[i2][1]
            else:
                if t % csf[i2][2] != 0:
                    t = ((t // csf[i2][2]) + 1) * csf[i2][2]
            t += csf[i2][0]
        r[i1] = t

    p2d = lambda x: print(*x, sep="\n")
    p2d(r)

if __name__ == '__main__':
    main()

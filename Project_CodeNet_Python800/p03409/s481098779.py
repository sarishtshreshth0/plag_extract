def main():
    n, *abcd = map(int, open(0).read().split())
    red = list(zip(abcd[0:2 * n + 1:2], abcd[1:2 * n + 1:2]))
    blue = list(zip(abcd[2 * n::2], abcd[2 * n + 1::2]))

    r = sorted(red, key=lambda p: p[1], reverse=True)
    b = sorted(blue)
    r = tuple(r)
    b = tuple(b)
    ans = 0
    done = []
    for xb, yb in b:
        for xr, yr in r:
            if xr < xb and yr < yb:
                if [xr, yr] not in done:
                    done.append([xr, yr])
                    ans += 1
                    break
    print(ans)


if __name__ == "__main__":
    main()

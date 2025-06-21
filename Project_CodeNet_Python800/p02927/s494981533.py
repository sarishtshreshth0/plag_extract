def main():
    import sys
    import bisect
    from itertools import accumulate

    m, d = map(int, input().split())
    if d < 22:
        print(0)
        return

    count = 0
    for i in range(22, d + 1):
        d1 = int(str(i)[1])
        d10 = int(str(i)[0])

        x = d1 * d10
        if 1 <= x <= m and d1 >= 2:
            count += 1
    print(count)


if __name__ == '__main__':
    main()

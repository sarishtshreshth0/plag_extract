def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))

    if m <= n:
        print(0)
        return

    x.sort()
    d = []
    for i in range(m-1):
        d.append(abs(x[i+1]-x[i]))

    d.sort()

    print(sum(d[0:(m-n)]))
    return


if __name__ == '__main__':
    main()
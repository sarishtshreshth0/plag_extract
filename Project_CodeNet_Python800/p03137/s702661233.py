def main():
    n, m = map(int, input().split())
    Xs = sorted(list(map(int, input().split())))
    Xs_diff = []
    if n >= m:
        print(0)
        exit()

    for i in range(1, m):
        Xs_diff.append(Xs[i]-Xs[i-1])

    Xs_diff.sort()
    ans = sum(Xs_diff[:(m-n)])
    print(ans)


if __name__ == "__main__":
    main()

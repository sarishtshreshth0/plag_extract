def main():
    n, m = map(int, input().split())
    xs = list(map(int, input().split()))
    if n >= m:
        print(0)
        exit()
    xs = sorted(xs)
    diff_xs = sorted([xs[i+1] - xs[i] for i in range(m-1)])
    ans = sum(diff_xs[:m-n])
    print(ans)


if __name__ == "__main__":
    main()

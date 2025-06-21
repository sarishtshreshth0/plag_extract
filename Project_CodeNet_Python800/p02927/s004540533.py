def main():
    M, D = map(int, input().split())
    ans = 0

    for d in range(22, D + 1):
        d1 = d % 10
        d10 = d // 10

        if d1 < 2 or d10 < 2:
            continue

        if 4 <= d10 * d1 <= M:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()

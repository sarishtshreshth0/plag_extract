def main():
    n, k = map(int, input().split())
    a = 1
    b = 0

    while True:
        a *= k
        if a > n:
            break
        b += 1

    ans = b + 1
    print(ans)


if __name__ == "__main__":
    main()

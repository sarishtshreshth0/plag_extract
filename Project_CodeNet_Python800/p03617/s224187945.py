def main():
    q, h, s, d = map(int, input().split())
    n = int(input())

    if n % 2 == 0:
        print(min(8 * q, 4 * h, 2 * s, d) * (n // 2))
    else:
        print(min(8 * q, 4 * h, 2 * s, d) * (n // 2) + min(4 * q, 2 * h, s))


if __name__ == "__main__":
    main()

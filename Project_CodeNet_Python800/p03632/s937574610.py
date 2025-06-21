def main():
    a, b, c, d = map(int, input().split())

    if b <= c:
        ans = 0
    elif d <= a:
        ans = 0
    else:
        if c <= a:
            if d <= b:
                ans = d - a
            else:
                ans = b - a
        else:
            if b <= d:
                ans = b - c
            else:
                ans = d - c

    print(ans)


if __name__ == "__main__":
    main()

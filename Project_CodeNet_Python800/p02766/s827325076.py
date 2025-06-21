# vim: fileencoding=utf-8


def main():
    n, k = map(int, input().split())
    ans = 0
    while True:
        t = n - k ** ans
        if t == 0:
            print(ans + 1)
            return
        if t < 0:
            print(ans)
            return
        ans += 1


if __name__ == "__main__":
    main()

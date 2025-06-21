# vim: fileencoding=utf-8


def main():
    n = int(input())
    ans = len(str(n))
    for a in range(2, int(pow(n, 0.5) + 1)):
        if n % a != 0:
            continue
        b = n // a
        l = max(len(str(a)), len(str(b)))
        if ans > l:
            ans = l
    print(ans)


if __name__ == "__main__":
    main()

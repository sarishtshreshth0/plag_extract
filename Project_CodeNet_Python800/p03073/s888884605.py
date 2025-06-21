def main():
    s = list(input())
    n = len(s)
    cnt0, cnt1 = 0, 0

    for i in range(n):
        if i % 2 == 0 and s[i] != "0":
            cnt0 += 1
        elif i % 2 == 1 and s[i] != "1":
            cnt0 += 1

    for i in range(n):
        if i % 2 == 0 and s[i] != "1":
            cnt1 += 1
        elif i % 2 == 1 and s[i] != "0":
            cnt1 += 1

    print(min(cnt0, cnt1))


if __name__ == "__main__":
    main()

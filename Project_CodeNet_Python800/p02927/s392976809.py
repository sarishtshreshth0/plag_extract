def main():
    M, D = (int(i) for i in input().split())
    ans = 0
    for m in range(1, M+1):
        for d in range(10, D+1):
            s = str(d)
            d1 = int(s[1])
            d10 = int(s[0])
            if d1 >= 2 and d10 >= 2 and m == d1*d10:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()

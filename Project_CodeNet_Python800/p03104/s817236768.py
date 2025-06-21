def main():
    A, B = (int(i) for i in input().split())

    def f(X):
        X += 1
        bi = []
        d = 2
        for i in range(40):
            v = (X//d) * (d//2) + max((X % d) - (d//2), 0)
            bi.append(v)
            d *= 2
        return bi

    ans = 0
    d = 0
    fA = f(A-1)
    fB = f(B)
    # print(fA, fB, sep="\n")
    for a, b in zip(fA, fB):
        v = max(b - a, 0)
        if v % 2 == 1:
            ans += 2**d
        d += 1
    print(ans)


if __name__ == '__main__':
    main()

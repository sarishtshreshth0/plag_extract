def main():
    a, b = map(int, input().split())

    # f(A, B) = f(0, a-1) ^ f(0, b) = F(a-1) ^ F(b)
    def F(x):
        if x % 2 == 0:
            if x % 4 == 0:
                return x
            else:
                return x ^ 1
        else:
            if (x + 1) % 4 == 0:
                return 0
            else:
                return 1

    print(F(a-1) ^ F(b))

main()
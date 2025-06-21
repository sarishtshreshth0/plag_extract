def main():
    MOD = 10 ** 9 + 7

    def choose(n, a, mod=MOD):
        x, y = 1, 1
        for i in range(a):
            x = x * (n - i) % mod
            y = y * (i + 1) % mod
        return x * pow(y, mod - 2, mod) % mod

    N, A, B = map(int, input().split())

    ans = pow(2, N, MOD) - choose(N, A) - choose(N, B) - 1  # 0本の組み合わせを差し引く
    ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()

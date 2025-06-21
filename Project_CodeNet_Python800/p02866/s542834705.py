def main():
    MOD = 998244353
    N = int(input())
    D = list(map(int, input().split(' ')))
    max_d = max(D)
    counter = [0] * (max_d + 1)
    for d in D:
        counter[d] += 1
    if D[0] != 0 or counter[0] != 1:
        print(0)
        return
    ans = 1
    for d in range(1, max_d + 1):
        ans *= pow(counter[d - 1], counter[d], MOD)
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()
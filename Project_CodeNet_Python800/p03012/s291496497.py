def main():
    N = int(input())
    W = list(map(int, input().split()))
    ans = 10 ** 10
    lst = [0 for _ in range(N)]
    lst[0] = W[0]

    for i in range(1, N):
        lst[i] = lst[i - 1] + W[i]

    for T in range(N - 1):
        S1 = lst[T]
        S2 = lst[-1] - lst[T]
        diff = abs(S1 - S2)
        if diff < ans:
            ans = diff

    print(ans)


if __name__ == "__main__":
    main()

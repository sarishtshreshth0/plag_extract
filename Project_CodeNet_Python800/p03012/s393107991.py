def main():
    N = int(input())
    W = list(map(int, input().split()))
    ans = 10 ** 10

    for T in range(N - 1):
        S1 = sum(W[:T + 1])
        S2 = sum(W[T + 1:])
        diff = abs(S1 - S2)
        if diff < ans:
            ans = diff

    print(ans)


if __name__ == "__main__":
    main()

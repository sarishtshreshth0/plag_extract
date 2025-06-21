def calc_digits(num):
    ans = 1
    while True:
        if num // 10 == 0:
            break
        num //= 10
        ans += 1

    return ans


def main():
    N = int(input())
    ans = 10 ** 10

    for A in range(1, int(N ** 0.5) + 1):
        if N % A != 0:
            continue
        B = N // A
        A_digits = calc_digits(A)
        B_digits = calc_digits(B)

        max_digits = max(A_digits, B_digits)
        if max_digits < ans:
            ans = max_digits

    print(ans)


if __name__ == "__main__":
    main()

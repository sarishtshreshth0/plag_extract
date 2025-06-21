def main():
    n = int(input())
    digit_sum = 0
    now = n
    while now > 0:
        digit_sum += now % 10
        now //= 10
    print("Yes" if n % digit_sum == 0 else "No")


if __name__ == '__main__':
    main()


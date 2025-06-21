from math import gcd


def main():
    n = int(input())
    a = list(map(int, input().split()))
    left_accumulate_gcd = [0 for _ in range(n + 2)]
    right_accumulate_gcd = [0 for _ in range(n + 2)]
    for i in range(n):
        left_accumulate_gcd[i + 1] = gcd(a[i], left_accumulate_gcd[i])
    for i in range(n - 1, -1, -1):
        right_accumulate_gcd[i] = gcd(a[i], right_accumulate_gcd[i + 1])
    ans = 1
    for i in range(n + 1):
        ans = max(ans, gcd(left_accumulate_gcd[i], right_accumulate_gcd[i + 1]))
    print(ans)


if __name__ == '__main__':
    main()


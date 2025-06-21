# coding: utf-8


def main():
    Q, H, S, D = map(int, input().split())
    N = int(input())
    ans = 0
    Q *= 4
    H *= 2
    min_price = min([Q, H, S])
    if N % 2 == 1:
        ans += min_price
    ans += N // 2 * min(min_price * 2, D)

    print(ans)

if __name__ == "__main__":
    main()

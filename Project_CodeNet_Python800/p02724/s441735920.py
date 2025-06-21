def main():
    x = int(input())

    coin_500 = x // 500
    coin_5 = x % 500 // 5

    ans = coin_500 * 1000 + coin_5 * 5

    print(ans)


if __name__ == "__main__":
    main()

def answer(x: int) -> int:
    dict = {500: 1000, 5: 5}
    happiness = 0

    for coin in sorted(dict, reverse=True):
        q, x = divmod(x, coin)
        happiness += dict[coin] * q

    return happiness


def main():
    x = int(input())
    print(answer(x))


if __name__ == '__main__':
    main()
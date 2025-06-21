def main(a: int, b: int, c: int):
    if a < c < b:
        print('Yes')
    elif a > c > b:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    a, b, c = map(int, input().split())

    main(a, b, c)

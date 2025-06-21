def main():
    X = int(input())

    p, r = divmod(X, 500)
    q, r = divmod(r, 5)
    print(p * 1000 + q * 5)


if __name__ == '__main__':
    main()

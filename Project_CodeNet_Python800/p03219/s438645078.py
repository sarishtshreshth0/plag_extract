def main():
    X, Y = map(int, input().split())
    print(X + (Y >> 1))


if __name__ == '__main__':
    main()

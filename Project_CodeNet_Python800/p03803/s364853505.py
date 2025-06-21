
def main():
    a, b = map(int, input().split())
    if a-2 < 0:
        a = 14

    if b-2 < 0:
        b = 14

    if a-2 > b-2:
        print('Alice')
    elif a-2 < b-2:
        print('Bob')
    else:
        print('Draw')


if __name__ == "__main__":
    main()


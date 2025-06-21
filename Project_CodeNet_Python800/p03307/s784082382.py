#!python3

# input
N = int(input())


def main():
    if N % 2 == 0:
        ans = N
    else:
        ans = 2 * N
    print(ans)


if __name__ == "__main__":
    main()

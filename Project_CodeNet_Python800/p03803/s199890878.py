#!python3

LI = lambda: list(map(int, input().split()))

# input
A, B = LI()


def main():
    a = 100 if A == 1 else A
    b = 100 if B == 1 else B
    if a > b:
        ans = "Alice"
    elif a < b:
        ans = "Bob"
    else:
        ans = "Draw"
    print(ans)


if __name__ == "__main__":
    main()

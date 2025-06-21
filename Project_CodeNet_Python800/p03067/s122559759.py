from sys import stdin


def answer(x, y, C):
    if x < C < y:
        print("Yes")
    else:
        print("No")


def main():
    A, B, C = [int(x) for x in stdin.readline().split()]
    if A < B:
        answer(A, B, C)
    else:
        answer(B, A, C)


if __name__ == "__main__":
    main()

import sys

input = sys.stdin.readline


def main():
    A, B = map(int, input().split())

    if (A * B) % 2 == 1:
        ans = "Yes"
    else:
        ans = "No"

    print(ans)


if __name__ == "__main__":
    main()

import sys

input = sys.stdin.readline


def main():
    N = int(input())
    S = input().rstrip()

    ans = ""
    n_left = 0
    n_right = 0
    for s in S:
        if s == "(":
            n_left += 1
        else:
            if n_left > 0:
                n_left -= 1
            else:
                n_right += 1

    ans = "".join(("(" * n_right, S, ")" * n_left))
    print(ans)


if __name__ == "__main__":
    main()

import math


def resolve():
    import sys
    input = sys.stdin.readline
    row1 = [int(x) for x in input().rstrip().split(" ")]
    h = row1[0]
    w = row1[1]

    if h == 1 or w == 1:
        print(1)
        return

    ans = (h-(h%2))*(w-(w%2))/2
    ans += (h%2)*(w-(w%2))/2
    ans += (w%2)*(h-(h%2))/2
    ans += (w%2)*(h%2)

    print(int(ans))


if __name__ == "__main__":
    resolve()

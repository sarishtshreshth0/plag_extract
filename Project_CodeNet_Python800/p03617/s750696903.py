# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    q, h, s, d = [int(x) for x in input().rstrip().split(" ")]
    n = int(input().rstrip())

    h = h if h < 2 * q else 2 * q
    s = s if s < 2 * h else 2 * h
    d = d if d < 2 * s else 2 * s

    ans = 0

    ans += (n // 2) * d
    n = n % 2

    ans += n * s

    print(ans)


if __name__ == "__main__":
    resolve()

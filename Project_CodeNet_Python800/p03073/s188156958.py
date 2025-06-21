
def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    s = input().rstrip()

    pattern1 = 0
    pattern2 = 0

    for i, c in enumerate(s):
        if i % 2 == 0:
            if c == "0":
                pattern1 += 1
            else:
                pattern2 += 1
        else:
            if c == "0":
                pattern2 += 1
            else:
                pattern1 += 1

    print(min(pattern1, pattern2))

if __name__ == "__main__":
    resolve()

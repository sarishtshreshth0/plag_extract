
def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())

    a, b = [int(x) for x in input().rstrip().split(" ")]
    s = input().rstrip()

    if str.isdecimal(s[0:a]) and str.isdecimal(s[a+1: len(s)]) and s[a] == "-":
        print("Yes")
    else:
        print("No")




if __name__ == "__main__":
    resolve()

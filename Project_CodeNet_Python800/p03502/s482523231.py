import sys
def input(): return sys.stdin.readline().strip()


def main():
    n = input()
    d = 0
    for c in n: d += int(c)
    if int(n) % d == 0:
        print("Yes")
    else:
        print("No")



if __name__ == "__main__":
    main()

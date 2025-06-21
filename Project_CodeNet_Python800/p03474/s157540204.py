import sys
def input(): return sys.stdin.readline().strip()


def main():
    a, b = map(int, input().split())
    s = input()
    for i in range(a + b + 1):
        if i != a and s[i] == '-':
            print("No")
            return
        elif i == a and s[i] !='-':
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()

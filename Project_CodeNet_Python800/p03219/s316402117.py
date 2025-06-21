import sys
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())
MII = lambda: list(map(int, IS().split()))

def main():
    x, y = MII()
    print(x+y//2)

if __name__ == '__main__':
    main()

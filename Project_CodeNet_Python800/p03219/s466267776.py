import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    X, Y = map(int, input().split())
    print(X + Y // 2)

if __name__ == '__main__':
    main()

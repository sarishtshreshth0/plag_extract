import sys
def input(): return sys.stdin.readline().strip()

def main():
    N = int(input())
    n = int(N ** 0.5) + 1
    ans = 10**18
    for a in range(n, 0, -1):
        if N % a != 0: continue
        b = str(N // a)
        print(len(b))
        return

if __name__ == "__main__":
    main()

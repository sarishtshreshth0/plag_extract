import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    s = list(input())
    ans = 0
    for i in range(1, n):
        if s[i] != s[i-1]:
            ans += 1
    print(ans+1)

if __name__ == '__main__':
    main()
import sys

input = sys.stdin.readline

def main():
    Q, H, S, D = map(int, input().split())
    N = int(input())
    ans = N//2*min(8*Q, 4*H, 2*S, D) + N%2*min(4*Q, 2*H, S)

    print(ans)

if __name__ == '__main__':
    main()
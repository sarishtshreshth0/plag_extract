import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    Q, H, S, D = [int(x) for x in input().split()]
    N = int(input())

    ans = 0
    if Q * 8 > D and H * 4 > D and S * 2 > D:
        X, N = divmod(N, 2)
        ans += X * D

    if Q * 4 > S and H * 2 > S:
        print(ans + S * N)
    elif Q * 2 > H:
        print(ans + H * 2 * N)
    else:
        print(ans + Q * 4 * N)


    
    

if __name__ == '__main__':
    main()


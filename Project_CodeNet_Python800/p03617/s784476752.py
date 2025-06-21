def myAnswer(Q: int, H: int, S: int, D: int, N: int) -> int:
    H = min(H, Q*2)
    S = min(S, H*2)
    D = min(D, S*2)
    total = 0
    while N != 0:
        if(N < 2):
            total += S
            N -= 1
        else:
            total += (N//2) * D
            N = N % 2
    return total


def modelAnswer():
    tmp = 1


def main():
    Q, H, S, D = map(int, input().split())
    N = int(input())
    print(myAnswer(Q, H, S, D, N))


if __name__ == '__main__':
    main()
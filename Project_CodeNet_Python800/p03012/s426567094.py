# -*- coding: utf-8 -*-

def main():

    N = int(input())
    W = list(map(int, input().split()))

    absW = []

    for i in range(N):
        absW.append(abs(sum(W[:i + 1]) - sum(W[i + 1:])))

    ans = min(absW)

    print(ans)


if __name__ == "__main__":
    main()
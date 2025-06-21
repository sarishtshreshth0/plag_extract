#!/usr/bin/env python3
def main():
    N, K = map(int, input().split())

    for i in range(10 ** 9):
        if N <= K ** i - 1:
            print(i)
            break


if __name__ == '__main__':
    main()

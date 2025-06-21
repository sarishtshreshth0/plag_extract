#!/usr/bin/env python3
def main():
    X = int(input())

    res = X // 500
    print(res * 1000 + (X - res * 500) // 5 * 5)


if __name__ == '__main__':
    main()

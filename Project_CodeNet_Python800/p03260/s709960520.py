# coding: utf-8

# https://atcoder.jp/contests/abc109
# 18:15-


def main():
    a, b = map(int, input().split())
    if a % 2 == 1 and b % 2 == 1:
        return "Yes"
    else:
        return "No"


print(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    CD = [list(map(int, input().split())) for _ in range(N)]

    reds = sorted(AB, key=lambda x: x[1], reverse=True)
    blues = sorted(CD, key=lambda x: x[0])
    cnt = 0

    for blue in blues:
        for red in reds:
            if red[0] < blue[0] and red[1] < blue[1]:
                red[1] = float("inf")
                cnt += 1
                break
    print(cnt)


if __name__ == "__main__":
    main()

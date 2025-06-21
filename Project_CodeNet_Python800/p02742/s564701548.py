#!/usr/local/bin/python3
# https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_b
import math

H, W = map(int, input().split())

if 1 in [H, W]:
    print(1)
else:
    print(math.ceil(H*W/2))

# coding: utf-8

A, B, C, D = map(int, input().split(" "))


if D <= A or B <= C:
    print(0)
else:
    l = sorted([A, B, C, D])
    print(l[2] - l[1])

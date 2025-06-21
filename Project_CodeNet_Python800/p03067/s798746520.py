#coding:utf-8

A, B, C = (int(x) for x in input().split())

if A <= C <= B or B <= C <= A:
    print("Yes")
else:
    print("No")
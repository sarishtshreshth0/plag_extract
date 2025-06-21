# coding: utf-8

data = list(map(lambda x: int(x), input().split(' ')))

if data[0] < data[2] < data[1] or data[0] > data[2] > data[1]:
    print("Yes")
else:
    print("No")
# -*- coding: utf-8 -*-

a, b = map(int, input().split())

a = 14 if a == 1 else a
b = 14 if b == 1 else b

if a > b:
    print('Alice')
elif a < b:
    print('Bob')
else:
    print('Draw')
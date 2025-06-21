# -*- coding: utf-8 -*-

A, B, C = map(int, input().split())

print('Yes' if A < C < B or B < C < A else 'No')

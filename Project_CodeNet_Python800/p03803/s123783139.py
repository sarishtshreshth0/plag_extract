# -*- coding: utf-8 -*-
A, B = map(lambda x: int(x) + (13 if x == '1' else 0), input().split())
print('Draw' if A == B else ['Bob', 'Alice'][A > B])
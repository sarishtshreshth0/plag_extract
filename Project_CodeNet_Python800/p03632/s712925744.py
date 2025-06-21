# -*- coding: utf-8 -*-

A, B, C, D = map(int, input().split())

late_start = 0
first_stop = 0
same_time = 0

late_start = max(A, C)
first_stop = min(B, D)
if first_stop - late_start > 0:
    same_time = first_stop - late_start
else:
    same_time = 0

print(same_time)
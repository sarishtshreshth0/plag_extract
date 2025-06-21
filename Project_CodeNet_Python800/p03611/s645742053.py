#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-06-26 15:12:37 +0900
# LastModified: 2020-06-26 15:33:28 +0900
#


import os
import sys
from collections import Counter
# import numpy as np
# import pandas as pd


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt_list = Counter(a)

    a_max = a[-1]
    a_min = a[0]
    cnt_max = 0
    for center in range(a_min-1, a_max+2):
        cnt = 0
        if center in cnt_list.keys():
            cnt += cnt_list[center]
        if center-1 in cnt_list.keys():
            cnt += cnt_list[center-1]
        if center+1 in cnt_list.keys():
            cnt += cnt_list[center+1]
        if cnt > cnt_max:
            cnt_max = cnt
    print(cnt_max)



if __name__ == "__main__":
    main()

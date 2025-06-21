#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-07-30 18:54:32 +0900
# LastModified: 2020-07-30 19:11:26 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd
def gcd(s, t):
    while t != 0:
        tmp = s % t
        s = t
        t = tmp
    return s


def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    a = []
    for i, s in enumerate(x):
        if i == 0:
            a.append(abs(x[0]-X))
            continue
        a.append(abs(x[i]-x[i-1]))
    ans = a[0]
    for i in range(1, len(a)):
        ans = gcd(max(ans, a[i]), min(ans, a[i]))
        
    print(ans)


if __name__ == "__main__":
    main()
